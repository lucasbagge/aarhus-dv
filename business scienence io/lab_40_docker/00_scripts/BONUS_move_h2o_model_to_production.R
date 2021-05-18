# LAB 40 - DOCKER FOR DATA SCIENCE
# MODULE: LLPRO BONUS - MLFLOW MOVE MODEL TO PRODUCTION

move_h2o_model_to_production <- function(path) {

    require(rlang)
    require(stringr)
    require(h2o)
    require(fs)
    require(crayon)

    if (is_missing(path)) abort("Please specify a path to the H2O model located in the artifacts > h2o folder")

    suppressWarnings(suppressMessages(h2o.init()))

    # Collect from MLFLow Artifacts
    path      <- file.path(rprojroot::find_rstudio_root_file(), path)
    h2o_model <- h2o.loadModel(path)

    # Production
    path_prod <- file.path(rprojroot::find_rstudio_root_file(), "00_production_model/")

    # Remove any models in production
    fs::dir_ls(path_prod) %>% map(fs::file_delete)

    # Save New Model in Production Folder
    h2o.saveModel(object = h2o_model, path = path_prod, force = TRUE)

    # Rename to PROD_H2O_MODEL
    temp_file_path <- fs::dir_ls(path_prod)[1]
    new_file_path  <- file.path(path_prod, "PROD_H2O_MODEL")
    fs::file_move(path     = temp_file_path,
                  new_path = new_file_path)

    rlang::inform(crayon::blue(str_glue(
"SUCCESS
----
Model has been copied to {path_prod}
")))

}
