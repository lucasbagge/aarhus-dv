# LAB 40 - DOCKER FOR DATA SCIENCE
# MODULE: LLPRO BONUS - MLFLOW GRID SEARCH TRACKING


run_h2o_grid_search_with_mlflow <- function(data, target, n_trees, max_depth,
                                            h2o_init = TRUE, launch_mlflow_ui = FALSE,
                                            mlflow_tracking_uri = "mlflow-lab-40",
                                            mlflow_experiment_name = "bankruptcy_prediction") {

    # CHECKS ----
    if (missing(data)) stop("Argument `data` is missing. Please provide `data`.")
    if (!is.data.frame(data)) stop("Argument `data` is not a data.frame. Please provide a data.frame.")

    if (missing(target)) stop("Argument `target` is missing. Please provide `target`.")
    if (!is.character(target)) stop("Argument `target` is not character. Please provide a single character for the target.")

    if (missing(n_trees)) stop("Argument `n_trees` is missing. Please provide `n_trees`.")
    if (!is.numeric(n_trees)) stop("Argument `n_trees` is not numeric. Please provide a numeric vector.")

    if (missing(max_depth)) stop("Argument `max_depth` is missing. Please provide `max_depth`.")
    if (!is.numeric(max_depth)) stop("Argument `max_depth` is not numeric. Please provide a numeric vector.")


    # LIBRARIES ----
    require(mlflow)
    require(carrier)
    require(h2o)
    require(tidyverse)
    require(fs)

    # INPUTS ----
    data_prepared_tbl <- data
    y <- target[1]
    x <- setdiff(names(data_prepared_tbl), y)
    # n_trees   <- c(25, 50, 100)
    # max_depth <- c(5, 10)

    # MLFLOW SETUP ----
    mlflow_set_tracking_uri(mlflow_tracking_uri)
    print(str_glue("MLFLOW TRACKING URI: {mlflow_get_tracking_uri()}\n"))

    mlflow_set_experiment(mlflow_experiment_name)
    print(str_glue("MLFLOW EXPERIMENT NAME: {mlflow_get_experiment()}\n"))

    # H2O SETUP ----
    if (h2o_init) h2o.init()

    parameter_grid <- expand_grid(n_trees, max_depth)

    # MLFLOW TRACKING (SEE LAB 39) ----
    for(i in 1:nrow(parameter_grid)) {

        param_n_trees   <- parameter_grid$n_trees[i]
        param_max_depth <- parameter_grid$max_depth[i]

        # Print Model Info
        print(
            str_glue(
                "H2O MODEL {i} of {nrow(parameter_grid)}
=====
N TREES: {param_n_trees}
MAX DEPTH: {param_max_depth}\n\n")
        )

        # MLFlow (See Lab 39)
        with(mlflow_start_run(), {

            # Create Model
            model <- h2o.randomForest(
                x = x,
                y = y,
                training_frame = as.h2o(data_prepared_tbl),
                ntrees    = param_n_trees,
                max_depth = param_max_depth,
                nfolds    = 5,
                seed      = 123
            )

            # Save Model in Temp Directory
            file      <- model@model_id
            full_path <- file.path(tempdir(), file)
            h2o.saveModel(model, path = full_path, force = TRUE) # Save in temp location

            # Create predictor
            predictor_crate  <- crate(~ as.data.frame(h2o::h2o.predict(!!model, h2o::as.h2o(.x))), !!model)

            # Calculate Metrics
            auc     <- h2o.auc(model, xval = TRUE)
            aucpr   <- h2o.aucpr(model, xval = TRUE)
            logloss <- h2o.logloss(model, xval = TRUE)

            # LOGS
            mlflow_log_param("n_trees", param_n_trees)
            mlflow_log_param("max_depth", param_max_depth)

            mlflow_log_metric("auc", auc)
            mlflow_log_metric("aucpr", aucpr)
            mlflow_log_metric("logloss", logloss)

            mlflow_log_model(model = predictor_crate, artifact_path = "predictor")
            mlflow_log_artifact(path = full_path, artifact_path = "h2o")

            unlink(full_path)
        })

    }

    if (launch_mlflow_ui) mlflow_ui()

}

