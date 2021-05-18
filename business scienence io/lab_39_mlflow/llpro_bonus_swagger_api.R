# LAB 39 - BANKRUPTCY PREDICTION API WITH MLFLOW
# MODULE: LLPRO BONUS - SWAGGER API

serve_model <- function(uri_name, experiment_id, run_id) {
    require(mlflow)
    require(rlang)
    require(stringr)
    require(h2o)
    require(fs)

    if (is_missing(uri_name)) abort("uri_name is the top level folder (e.g. lab-39)")
    if (is_missing(experiment_id)) abort("experiment_id is the 2nd-level folder (e.g. 1)")
    if (is_missing(run_id)) abort("run_id is the 3rd-level folder (e.g. 996fe2b78c194d73a4e8b7ac43128a4e)")

    project_path <- stringr::str_c(uri_name, "/", experiment_id, "/", run_id)
    print(project_path)

    # Fire up H2O
    h2o.init()

    # Load Model - Required to serve your predictor
    model_path <- dir_ls(str_glue("{project_path}/artifacts/h2o"))
    h2o.loadModel(model_path)

    # Run Swagger using your stored model
    mlflow_rfunc_serve(str_glue("{project_path}/artifacts/predictor"))
}
