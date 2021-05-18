# LAB 39 - BANKRUPTCY PREDICTION API WITH MLFLOW
# MODULE: LLPRO BONUS - UMAP VISUALIZATION
# NOTE - UMAP IS COVERED IN DS4B 101-R

# Libraries ----
library(recipes)
library(embed)
library(tidyverse)
library(tidyquant)
library(plotly)

# Data ----
data_tbl <- read_rds("data/bankruptcy_data.rds")
data_dictionary_raw_tbl <- read_rds("data/data_dictionary_raw_tbl.rds")

# Data Prep ----
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

# Apply UMAP ----
recipe_spec <- recipe(class ~ ., data_prepared_tbl) %>%
    step_normalize(contains("Attr")) %>%
    step_umap(contains("Attr"), outcome = vars(class), num_comp = 3, seed = c(123, 123))

umap_data_tbl <- recipe_spec %>% prep() %>% juice()

umap_data_tbl

# Create tooltip/Hover ----
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

# Plotly Visualization ----
plot_data_tbl %>%
    plot_ly(x = ~ umap_1, y = ~ umap_2, z = ~ umap_3,
            color = ~ class, colors = c('#BF382A', '#0C4B8E'),
            hovertemplate = ~ tooltip) %>%
    add_markers(opacity = 0.5)
