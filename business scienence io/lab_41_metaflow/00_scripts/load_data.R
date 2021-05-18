load_data <- function(self) {

    # Tell us which backend we are using
    message("Using metadata provider: ", metaflow::get_metadata())

    message("Installing Dependencies...")
    source("00_scripts/install_dependencies.R")
    install_dependencies()

    suppressPackageStartupMessages(require(tidyverse))

    message("Loading Data...")

    self$data <- read_rds("./00_data/category_sales_tbl.rds") %>%
        group_by(Product_Category) %>%
        mutate(Date = as.character(Date)) # Avoid Type Conversion until build_glmnet_model()

    self$groups <- unique(self$data$Product_Category)

}
