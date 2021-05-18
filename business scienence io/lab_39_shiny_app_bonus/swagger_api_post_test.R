# LAB 39 - BANKRUPTCY PREDICTION API WITH MLFLOW
# MODULE: LLPRO BONUS - SWAGGER API TEST
# !! IMPORTANT NOTE: The Swagger API must be served on a separate R Session using the serve_model() function

# Libraries ----
library(tidyverse)
library(httr)
library(jsonlite)

# API URL ----
url <- "http://127.0.0.1:8090/"
full_path <- str_c(url, "predict/")

id <- "5899"

# Prep Data ----
data_tbl <- read_rds("data/bankruptcy_data.rds")

data_prepared_tbl <- data_tbl %>%
    rowid_to_column(var = ".id") %>%
    select(-Attr37) %>%
    drop_na()

# Hit Swagger API ----
resp <- httr::POST(
    url  = str_c(url, "predict/"),
    body = data_prepared_tbl %>% filter(as.character(.id) == id) %>% select(-.id, -class) %>% toJSON(),
    encode = "json"
)

# Review Prediction ----
prediction_tbl <- content(resp) %>% pluck(1) %>% as_tibble()

prediction_tbl



