# LAB 39 - BANKRUPTCY PREDICTION API WITH MLFLOW
# MODULE: LLPRO BONUS - SHINY APP
# !! IMPORTANT NOTE: The Swagger API must be served on a separate R Session using the serve_model() function

# LIBRARIES ----
library(shiny)
library(shinythemes)
library(httr)
library(jsonlite)
library(recipes)
library(embed)
library(tidyverse)
library(tidyquant)
library(plotly)

# API PATH ----
url <- "http://127.0.0.1:8090/"
full_path <- str_c(url, "predict/")

id <- "5899"

# DATA PREPROCESSING ----

data_tbl <- read_rds("data/bankruptcy_data.rds")
data_dictionary_raw_tbl <- read_rds("data/data_dictionary_raw_tbl.rds")

# * Data Prep ----
data_prepared_tbl <- data_tbl %>%
    rowid_to_column(var = ".id") %>%
    select(-Attr37) %>%
    drop_na()

data_dictionary_tbl <- data_dictionary_raw_tbl %>%
    separate(
        `Attribute.Information:`,
        into = c("id", "desc"),
        sep = " ",
        extra = "merge"
    ) %>%
    mutate(id = str_replace(id, "X", "Attr"))

# * Apply UMAP ----
recipe_spec <- recipe(class ~ ., data_prepared_tbl) %>%
    step_normalize(contains("Attr")) %>%
    step_umap(contains("Attr"), outcome = vars(class), num_comp = 3, seed = c(123, 123))

umap_data_tbl <- recipe_spec %>% prep() %>% juice()

# * Create tooltip/Hover ----
plot_data_tbl <- umap_data_tbl %>%
    left_join(
        data_prepared_tbl %>%
            select(.id, Attr39, Attr56, Attr26, Attr22)
    ) %>%
    mutate(tooltip = str_glue(
        "
        Company ID: {.id}
        Class: {class}
        Attr 39 Profit on Sales / Sales: {Attr39}
        Attr 26 (net profit + depreciation) / total liabilities: {Attr26}
        Attr 22 profit on operating activities / total assets: {Attr22}
        Attr56 (sales - cost of products sold) / sales: {Attr56}
        "
    ))

# UI FUNCTIONS ----
info_card <- function(title, value, sub_value,
                      main_icon = "chart-line", sub_icon = "arrow-up",
                      bg_color = "default", text_color = "default",
                      sub_text_color = "success") {

    require(tidyverse)
    require(shiny)

    div(
        class = "panel panel-default",
        style = "padding: 0px;",
        div(
            class = str_glue("panel-body bg-{bg_color} text-{text_color}"),
            p(class = "pull-right", icon(class = "fa-4x", main_icon)),
            h4(title),
            h5(value),
            p(
                class = str_glue("text-{sub_text_color}"),
                icon(sub_icon),
                tags$small(sub_value)
            )
        )
    )

}

# ---- 1.0 UI ----
ui <- navbarPage(
    title = "H2O & MLFlow Bankruptcy API",
    collapsible = TRUE,
    inverse     = FALSE,
    theme       = shinytheme("flatly"),

    shiny::tabPanel(
        title = "Bankruptcy Explorer",
        sidebarLayout(
            sidebarPanel(
                width = 3,
                h3("Company Risk Assessment"),
                HTML("<p>The company analysis tool connects to a <code>H2O</code> Random Forest Model being served
                  via <code>MLFlow</code> Swagger API. The model is running on a separate R Session.
                  This app connects to the API and generates a real-time bankruptcy risk assessment for the Company ID selected.</p>"),
                hr(),
                uiOutput("cards"),
                hr(),
                shiny::textInput(inputId = "company_id", label = "Company ID", value = id),
                shiny::actionButton(inputId = "submit", "Submit", class = "btn-primary")
            ),

            # Show a plot of the generated distribution
            mainPanel(
                width = 9,
                div(
                    class = "row",
                    div(
                        class = "col-sm-12 panel",
                        div(class = "panel-heading", h5("Corporation Bankruptcy Explorer")),
                        div(
                            class = "panel-body",
                            plotlyOutput(outputId = "plotly", height = "800px")
                        )
                    )
                ),

                # # Used for debugging
                # verbatimTextOutput(outputId = "code")


            )
        )

    )

)

# ---- 2.0 SERVER ----
server <- function(session, input, output) {

    # 2.1 Setup Reactive Values ----
    rv <- reactiveValues()

    observeEvent(input$submit, {

        rv$plot_data_tbl <- plot_data_tbl

        resp <- httr::POST(
            url  = str_c(url, "predict/"),
            body = data_prepared_tbl %>%
                filter(as.character(.id) == input$company_id) %>%
                select(-.id, -class) %>% toJSON(),
            encode = "json"
        )

        rv$prediction_tbl <- content(resp) %>% pluck(1) %>% as_tibble()


    }, ignoreNULL = FALSE)

    # 2.2 Debugging ----
    output$code <- renderPrint({
        # Used for debugging
        list(
            plot_data_tbl  = rv$plot_data_tbl,
            prediction_tbl = rv$prediction_tbl
        )
    })

    # 2.3 Plotly ----
    output$plotly <- renderPlotly({

        req(rv$plot_data_tbl)

        rv$plot_data_tbl %>%
            plot_ly(x = ~ umap_1, y = ~ umap_2, z = ~ umap_3,
                    color = ~ class, colors = c('#BF382A', '#0C4B8E'),
                    hovertemplate = ~ tooltip) %>%
            add_markers(opacity = 0.5)

    })

    # 2.4 Info Cards ----
    output$cards <- renderUI({
        req(rv$prediction_tbl)

        p1 <- rv$prediction_tbl$p1

        div(
            info_card(
                title = "Bankruptcy Prediction Risk",
                value = scales::percent(p1),
                sub_value = ifelse(p1 < 0.15, "Risk is Low", "Risk is HIGH"),
                main_icon = "chart-line",
                sub_icon = ifelse(p1 < 0.15, "arrow-down", "arrow-up"),
                bg_color = "primary",
                text_color = "success",
                sub_text_color = ifelse(p1 < 0.15, "success", "danger")
            )
        )
    })


}

# Run the application
shinyApp(ui = ui, server = server)
