compute_models <- function(self) {

    suppressPackageStartupMessages(require(tidyverse))

    source("00_scripts/build_glmnet_model.R")

    message("Computing Models...")

    self$group <- self$input
    message("Computing models for ", self$group)

    df <- self$data

    data_by_category <- df %>%
        filter(Product_Category == self$input) %>%
        ungroup()

    self$forecast <- build_glmnet_model(
        data    = data_by_category,
        assess  = "12 weeks",
        penalty = 0.1,
        mixture = 0.5
    )

}
