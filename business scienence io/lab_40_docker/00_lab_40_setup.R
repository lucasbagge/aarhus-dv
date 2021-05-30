# LAB 40 - DOCKER FOR DATA SCIENCE
# MODULE: H2O GRID SEARCH TRACKING WITH MLFLOW


# H2O VERSION 3.30.0.1 -----
# MAKE SURE H2O 3.30.0.1 is installed!!!
# devtools::install_version('h2o', version = '3.30.0.1', dependencies = TRUE)


# LIBRARIES ----
library(mlflow)
library(carrier)
library(h2o)
library(tidyverse)
library(fs)

# MLFLOW INSTALLATION ----
install_mlflow()

# DATA ----
data_prepared_tbl <- read_rds("00_data/data_prepared_tbl.rds")
data_prepared_tbl

# 1.0 [!!BONUS!!] H2O GRID SEARCH -----

# Source: run_h2o_grid_search_with_mlflow()
source("00_scripts/BONUS_h2o_grid_search_mlflow_tracking.R")

mlflow_ui()

# Iterate through Grid Search
run_h2o_grid_search_with_mlflow(

    data      = data_prepared_tbl,
    target    = "class",

    # H2O Grid Search
    h2o_init  = TRUE,
    n_trees   = c(25, 100),
    max_depth = c(5, 10),

    # MLFLOW
    launch_mlflow_ui       = TRUE,
    mlflow_tracking_uri    = "mlflow",
    mlflow_experiment_name = "Bankruptcy Prediction API"
)

# 2.0 [!!BONUS!!] SAVE BEST MODEL INTO PRODUCTION FOLDER ----

# Source: move_h2o_model_to_production()
source("00_scripts/BONUS_move_h2o_model_to_production.R")

# Copy model to production folder
move_h2o_model_to_production(
    path = "mlflow/1/1d50ae78d91c4502ba7c65b07d5f5909/artifacts/h2o/DRF_model_R_1621720317454_1353"
)




