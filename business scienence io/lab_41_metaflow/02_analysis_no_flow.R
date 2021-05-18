# LEARNING LAB 41: METAFLOW ----
# MODULE 02: NO METAFLOW ----

# 1.0 LIBRARIES ----

# Modeltime
library(tidymodels)
library(modeltime)
library(glmnet)

# Core
library(tidyverse)
library(timetk)
library(lubridate)


# 2.0 DATA ----

# * Pull Data ----
category_sales_tbl <- read_rds("00_data/category_sales_tbl.rds")

category_sales_tbl %>%
    group_by(Product_Category) %>%
    plot_time_series(Date, Order_Demand, .facet_ncol = 2, .smooth = F)

# 3.0 SINGLE GROUP ----

group <- "Category_005"

# * Filter Data ----
category_05_tbl <- category_sales_tbl %>%
    filter(Product_Category == group) %>%
    ungroup()

category_05_tbl %>%
    plot_time_series(Date, Order_Demand)


# 4.0 SUMMARY STATISTICS ----

order_demand        <- category_05_tbl %>% pull(Order_Demand)
order_demand_sum    <- sum(order_demand, na.rm = TRUE)
order_demand_mean   <- mean(order_demand, na.rm = TRUE)

tibble(
    Product_Category  = group,
    Order_Demand_Sum  = order_demand_sum,
    Order_Demand_Mean = order_demand_mean
)


# 5.0 TIME SERIES FORECAST ----

# * Train/Test Splits ----
splits <- time_series_split(category_05_tbl, assess = "12 weeks", cumulative = TRUE)

# * Recipe ----
recipe_spec <- recipe(Order_Demand ~ Date, training(splits)) %>%
    step_timeseries_signature(Date) %>%
    step_rm(matches("(.iso$)|(.xts$)|(hour)|(minute)|(second)|(am.pm)")) %>%
    step_fourier(Date, period = c(4, 16, 52), K = 2) %>%
    step_dummy(all_nominal())

# * Model ----
model_spec_glmnet <- linear_reg(penalty = 0.1, mixture = 0.5) %>%
    set_engine("glmnet")

# * Workflow ----
workflow_fit_glmnet <- workflow() %>%
    add_recipe(recipe_spec %>% step_rm(Date)) %>%
    add_model(model_spec_glmnet) %>%
    fit(training(splits))

# * Calibrate ----
calibration_tbl <- modeltime_table(
    workflow_fit_glmnet
) %>%
    modeltime_calibrate(testing(splits))

# * Accuracy ----
calibration_tbl %>% modeltime_accuracy()

# * Visualize ----
calibration_tbl %>%
    modeltime_forecast(
        new_data = testing(splits),
        actual_data = category_05_tbl
    ) %>%
    plot_modeltime_forecast(
        .y_intercept = 0,
        .y_intercept_color = "grey70"
    )

# * Forecast ----
refit_tbl <- calibration_tbl %>%
    modeltime_refit(category_05_tbl)

refit_tbl %>%
    modeltime_forecast(
        h = "12 weeks",
        actual_data = category_05_tbl
    ) %>%
    plot_modeltime_forecast(
        .y_intercept = 0,
        .y_intercept_color = "grey70"
    )
