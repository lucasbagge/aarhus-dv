build_glmnet_model <- function(data, assess = "12 weeks", penalty = 0.1, mixture = 0.5) {

    suppressPackageStartupMessages(require(tidymodels))
    suppressPackageStartupMessages(require(modeltime))
    suppressPackageStartupMessages(require(glmnet))
    suppressPackageStartupMessages(require(tidyverse))
    suppressPackageStartupMessages(require(recipes))
    suppressPackageStartupMessages(require(timetk))
    suppressPackageStartupMessages(require(lubridate))

    # Ensure Correct Data Type
    data <- data %>%
        mutate(Date = ymd(Date))

    print(head(data))

    # * Train/Test Splits ----
    splits <- time_series_split(data, assess = assess, cumulative = TRUE)

    # * Recipe ----
    recipe_spec <- recipe(Order_Demand ~ Date, data = training(splits)) %>%
        step_timeseries_signature(Date) %>%
        step_rm(matches("(.iso$)|(.xts$)|(hour)|(minute)|(second)|(am.pm)")) %>%
        step_fourier(Date, period = c(4, 16, 52), K = 2) %>%
        step_dummy(all_nominal())

    # * Model ----
    model_spec_glmnet <- linear_reg(
        penalty = penalty,
        mixture = mixture
    ) %>%
        set_engine("glmnet")

    # * Workflow ----
    workflow_glmnet <- workflow() %>%
        add_recipe(recipe_spec %>% step_rm(Date)) %>%
        add_model(model_spec_glmnet) %>%
        fit(training(splits))

    # * Modeltime ----
    calibration_tbl <- modeltime_table(
        workflow_glmnet
    ) %>%
        modeltime_calibrate(new_data = testing(splits))

    # accuracy_tbl <- calibration_tbl %>%
    #     modeltime_accuracy()

    refit_tbl <- calibration_tbl %>%
        modeltime_refit(data)

    forecast_tbl <- refit_tbl %>%
        modeltime_forecast(
            h           = assess,
            actual_data = data
        ) %>%
        mutate(.index = as.character(.index))

    return(forecast_tbl)

}
