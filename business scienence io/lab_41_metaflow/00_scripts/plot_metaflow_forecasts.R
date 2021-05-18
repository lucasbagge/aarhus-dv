plot_metaflow_forecasts <- function(flow_name = "ProductSalesForecast", run_id = "latest", plot = TRUE, ...) {

    flow <- metaflow::flow_client$new(flow_name)

    if (run_id == "latest") {
        run_id <- flow$latest_run
    }

    run <- flow$run(run_id)

    forecast_tbl <- run$artifact("forecast") %>%
        as_tibble() %>%
        mutate(.index = ymd(.index)) %>%
        group_by(Product_Category)

    if (plot) {
        ret <- forecast_tbl %>%
            plot_time_series(.index, .value, .key, .smooth = F, .facet_ncol = 2, ...)
    } else {
        ret <- forecast_tbl
    }

    return(ret)

}


