# Libraries & Setup ----
library(modeltime)
library(tidymodels)
library(tidyquant)
library(tidyverse)
library(lubridate)
library(timetk)
library(modeltime.ensemble)
library(slider)

# ---- SINGLE TIME SERIES (NON-PANEL) -----

# data----
# 
SPY_tibble <- tq_get("CHR.CO", get="stock.prices") %>% 
  select(c(date, close))


#  Create a split object ----
set.seed(314)

split <- SPY_tibble %>% time_series_split(assess = "3 months", cumulative = TRUE)

## Build training data set ----
train <- split %>% 
  training()

## Build testing data set ----
test <- split %>% 
  testing()

# Feature engineering ----

recipe <- recipe(close ~ ., data = train) %>% 
  step_timeseries_signature(date) %>%
  step_rm(matches("(iso$)|(xts$)|(day)|(hour)|(min)|(sec)|(am.pm)")) %>%
  step_mutate(Date_week = factor(date_week, ordered = TRUE)) %>%
  step_dummy(all_nominal()) %>%
  step_normalize(contains("index.num"), date_year) %>% 
  step_naomit(all_numeric())

recipe %>% prep() %>% juice()

# modelling ----
 
lm_model <- linear_reg() %>% 
  set_engine('lm') %>% # adds lm implementation of linear regression
  set_mode('regression')

model_fit_ets <- modeltime::exp_smoothing() %>%
  parsnip::set_engine(engine = "ets") %>%
  parsnip::fit(close ~ date, data = train)

# Prophet
model_fit_prophet <- modeltime::prophet_reg() %>%
  parsnip::set_engine("prophet") %>%
  parsnip::fit(
    close ~ date,
    data = train)

model_spec_nnetar <- nnetar_reg(
  seasonal_period = 52,
  non_seasonal_ar = 4,
  seasonal_ar     = 1) %>%
  set_engine("nnetar")

model_fit_prophet_boost <- modeltime::prophet_boost() %>%
  parsnip::set_engine("prophet_xgboost") %>%
  parsnip::fit(close ~ date + as.numeric(date) + month(date, label = TRUE),
               data = train)

model_spec_rf <-
  rand_forest(trees = 5000, min_n = 5000) %>%
  set_engine("randomForest")

# workflow ----

wf <-
  workflow() %>% 
  add_model(lm_model) %>% 
  add_recipe(recipe)

wflw_fit_nnetar <- 
  workflow() %>%
  add_model(model_spec_nnetar) %>%
  add_recipe(recipe) %>%
  fit(train)

workflow_fit_rf <- 
  workflow() %>%
  add_model(model_spec_rf) %>%
  add_recipe(recipe %>% step_rm(date)) %>%
  fit(train)


# evaluation ----

model_tbl <- modeltime_table(
  wf %>% fit(train),
  model_fit_ets,
  model_fit_prophet,
  wflw_fit_nnetar,
  workflow_fit_rf
)

# Calibrate the model accuracy using the hold out data
calibration_tbl <-
  model_tbl %>%
  modeltime_calibrate(test)

calibration_tbl %>%
  modeltime_accuracy() %>% 
  table_modeltime_accuracy(.interactive = FALSE)

calibration_tbl %>%
  modeltime_refit(SPY_tibble) %>% 
  modeltime_forecast(h = "2 months", 
                     actual_data = SPY_tibble %>% 
                       filter(date > "2021-03-01"),
                     conf_interval = 0.1) %>% 
  plot_modeltime_forecast(.interactive = TRUE)

# resursive ----

m750

m750 
SPY_tibble

SPY_tibble <- tq_get("CHR.CO", get="stock.prices") %>% 
  select(c(date, close, symbol)) %>%
  rename(value = close) %>% 
  mutate(id = as.factor(symbol)) %>% 
  select(-symbol)
FORECAST_HORIZON <- 24

m750_extended <- SPY_tibble %>%
  group_by(id) %>%
  future_frame(
    .length_out = FORECAST_HORIZON,
    .bind_data  = TRUE
  ) %>%
  ungroup()

# TRANSFORM FUNCTION ----
# - Function runs recursively that updates the forecasted dataset
lag_roll_transformer <- function(data){
  data %>%
    # Lags
    tk_augment_lags(value, .lags = 1:8) %>%
    # Rolling Features
    mutate(rolling_mean_12 = lag(slide_dbl(
      value, .f = mean, .before = 8, .complete = FALSE
    ), 1))
}

# Data Preparation
m750_rolling <- m750_extended %>%
  lag_roll_transformer() %>%
  select(-id)

train_data <- m750_rolling %>%
  drop_na()

future_data <- m750_rolling %>%
  filter(is.na(value))

# Modeling

# Straight-Line Forecast
model_fit_lm <- linear_reg() %>%
  set_engine("lm") %>%
  # Use only date feature as regressor
  fit(value ~ date, data = train_data)

# Autoregressive Forecast
model_fit_lm_recursive <- 
  boost_tree("regression", learn_rate = 0.35) %>%
  set_engine("xgboost") %>%
  fit(value ~ ., data = train_data) %>% 
  # Add recursive() w/ transformer and train_tail
  recursive(
    transform  = lag_roll_transformer,
    train_tail = tail(train_data, FORECAST_HORIZON)
  )

# Forecasting
modeltime_table(
  model_fit_lm,
  model_fit_lm_recursive
) %>%
  update_model_description(2, "LM - Lag Roll") %>%
  modeltime_forecast(
    new_data    = future_data,
    actual_data = SPY_tibble %>%  filter(date > "2021-01-01")
  ) %>%
  plot_modeltime_forecast(
    .interactive        = TRUE,
    .conf_interval_show = FALSE
  )


# ide ----
#  Tag andre tidserier med aktier osom er korrelerede.
#  
#  
# 