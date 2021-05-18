join_forecasts <- function(self, inputs) {

    suppressPackageStartupMessages(require(tidyverse))

    message("Joining Forecasts...")

    product_category_tbl <- tibble(
        Product_Category  = unlist(lapply(inputs, function(inp) {inp$group})),
        Forecast          = lapply(inputs, function(inp) {inp$forecast})
    )

    self$forecast <- product_category_tbl %>%
        unnest(Forecast) %>%
        mutate(.index = as.character(.index))

}
