# LEARNING LAB 41: METAFLOW ----
# MODULE 04: GROUPED TIME SERIES FORECASTING METAFLOW ----

# 1.0 LIBRARIES ----

# Scale
library(metaflow)

# Modeltime
library(tidymodels)
library(modeltime)
library(glmnet)

# Core
library(tidyverse)
library(timetk)
library(lubridate)

# 2.0 FUNCTIONS ----
# - LLPRO BONUS: GO PRO TO GET THESE FUNCTIONS THAT DO THE MULTI-FORECAST HEAVY LIFTING 💪
source("00_scripts/load_data.R")
source("00_scripts/compute_models.R")
source("00_scripts/join_forecasts.R")
source("00_scripts/summarize_flow.R")
source("00_scripts/plot_metaflow_forecasts.R")

# 3.0 META FLOW - Foreach ----

decorator_type <- "resources" # Local
# decorator_type <- "batch" # AWS

# * Flow ----
metaflow("ProductSalesForecast") %>%

    # Load Data
    metaflow::step(
        step       = "start",
        r_function = load_data,
        foreach    = "groups",
        next_step  = "compute_models") %>%

    # Compute Data Groups
    metaflow::step(
        step       = "compute_models",
        metaflow::decorator(decorator_type, cpu = 8, memory = 20000), # Local
        r_function = compute_models,
        next_step  = "join_forecasts") %>%

    # Compute Stats
    metaflow::step(
        step       = "join_forecasts",
        r_function = join_forecasts,
        join       = TRUE,
        next_step  = "end") %>%

    metaflow::step(
        step = "end",
        r_function = summarize_flow
    ) %>%

    metaflow::run()

# * Results ----
# - LLPRO BONUS: GO PRO TO GET THIS FUNCTION - Makes 5 forecasts automatically!!! 🤯

plot_metaflow_forecasts(
    flow_name = "ProductSalesForecast",
    run_id    = "latest",
    .y_intercept = 0,
    .y_intercept_color = "gray70"
)

flow <- flow_client$new("ProductSalesForecast")
flow$runs

flow$run(flow$latest_run)$artifact("forecast") %>% as_tibble()
