# LEARNING LAB 41: METAFLOW ----
# MODULE 03: SUMMARY STATS METAFLOW ----

# 1.0 LIBRARIES ----

library(metaflow)
library(tidyverse)
library(plotly)

# 2.0 FUNCTIONS ----

load_data <- function(self) {

    # Tell us which backend we are using
    message("Using metadata provider: ", metaflow::get_metadata())

    suppressPackageStartupMessages(require(tidyverse))

    message("Loading Data...")

    self$data   <- read_rds("./00_data/category_sales_tbl.rds") %>%
        group_by(Product_Category)

    self$groups <- unique(self$data$Product_Category)

}

# Compute statistics for a single genre.
compute_summary_stats <- function(self){

    suppressPackageStartupMessages(require(tidyverse))

    message("Computing Summary Statstics...")

    message("Computing statistics for ", self$input)

    # Save Temporary Input as "group" in each for-each loop
    self$group <- self$input

    # Save data by category in each for-each loop
    self$data_by_category <- self$data %>%
        filter(Product_Category == self$input) %>%
        ungroup()

    order_demand <- self$data_by_category %>% pull(Order_Demand)

    # Save sum & mean statistic for each for-each loop
    self$sum     <- sum(order_demand, na.rm = TRUE)
    self$mean    <- mean(order_demand, na.rm = TRUE)
}

join_summary_stats <- function(self, inputs) {

    suppressPackageStartupMessages(require(tidyverse))

    message("Joining Data...")

    # Aggregate the statistics for each input group
    self$summary <- tibble(
            Product_Category  = unlist(lapply(inputs, function(inp) {inp$group})),
            Order_Demand_Sum  = unlist(lapply(inputs, function(inp) {inp$sum})),
            Order_Demand_Mean = unlist(lapply(inputs, function(inp) {inp$mean}))
    )

}

summarize_stats <- function(self) {
    print(self$summary)
}


# 3.0 META FLOW - Foreach ----

# * MetaFlow ----
metaflow("ProductSalesSummary") %>%

    # Data
    metaflow::step(
        step       = "start",
        r_function = load_data,

        # For-each group
        foreach    = "groups",

        next_step  = "compute_stats") %>%

    # Compute Stats
    metaflow::step(
        step       = "compute_stats",

        # Specify resources (Local = "resources", AWS = "batch")
        metaflow::decorator("resources", cpu = 4, memory = 8000),

        r_function = compute_summary_stats,
        next_step  = "join_stats") %>%

    # Compute Stats
    metaflow::step(
        step       = "join_stats",
        r_function = join_summary_stats,

        # Joining step (tells metaflow to stop running in parallel)
        join       = TRUE,

        next_step  = "end") %>%

    metaflow::step(
        step = "end",
        r_function = summarize_stats
    ) %>%

    metaflow::run()


# 4.0 ACCESSING RESULTS ----

# * Flow Client - New
flow <- metaflow::flow_client$new("ProductSalesSummary")

# * Accessing Runs
flow$runs
run <- flow$run("1597863681370093")

run$artifacts


# * Accessing Artifacts (Results) ----
run$artifacts
sales_summary <- run$artifact("summary") %>% as_tibble()

# * Generating Information ----
sales_plot <- sales_summary %>%
    arrange(desc(Order_Demand_Sum)) %>%
    mutate(Product_Category = as_factor(Product_Category) %>% fct_rev()) %>%
    ggplot(aes(Product_Category, Order_Demand_Sum)) +
    geom_col(fill = "#2c3e50") +
    coord_flip() +
    scale_y_continuous(labels = scales::dollar) +
    theme_minimal() +
    labs(title = "Sales Demand", y = "", x = "Product Category")

sales_plot_interactive <- ggplotly(sales_plot)



