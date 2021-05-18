# LAB 42: PLUMBER API ----
# CRANLOGS API ----

# 1.0 LIBRARIES ----

library(plumber)
library(cranlogs)
library(tidyverse)
library(timetk)

# 2.0 MAIN FUNCTION ----

get_cran_data <- function(package = "dplyr", start = "2011-01-01", end = lubridate::today(), by = "day") {

    if (!by %in% c("day", "week", "month", "quarter", "year")) {
        by <- "day"
    }

    data_raw_tbl <- cran_downloads(
        packages = package,
        from     = as.character(start),
        to       = as.character(end)
    ) %>% as_tibble()

    data_prepared_tbl <- data_raw_tbl %>%
        group_by(package) %>%
        summarise_by_time(date, .by = by, count = sum(count, na.rm = TRUE))

    return(data_prepared_tbl)
}

# 3.0 ENDPOINTS ----

#* @apiTitle Cranlogs API



#    * /cran ----

#* Get the Raw Download Data
#* @param package The package to get download history
#* @param start The start date
#* @param end The end date
#* @param by The aggregation window
#*
#* @get /cran
function(package = "dplyr", start = "2011-01-01", end = lubridate::today(), by = "day") {

    list(
        data = get_cran_data(package, start, end, by)
    )
}

# * /cran/timeplot ----

#* Return a Plotly Time Series Plot
#*
#* @param package The package to get download history
#* @param start The start date
#* @param end The end date
#* @param by The aggregation window. Can be day, week, month, quarter, year.
#* @param show_smooth TRUE/FALSE. Toggle the smoother on/off. Default is TRUE.
#*
#* @get /cran/timeplot
#* @serializer htmlwidget
function(package = "dplyr", start = "2011-01-01", end = lubridate::today(), by = "day",
         show_smooth = TRUE, smooth_span = 0.75) {

    data_prepared_tbl <- get_cran_data(package, start, end, by)

    data_prepared_tbl %>%
        group_by(package) %>%
        plot_time_series(
            date, count,
            .title = str_glue("Package Downloads of: {package}"),
            .smooth = as.logical(show_smooth),
            .smooth_span = as.numeric(smooth_span)
        )
}


# * /cran/seasonalityplot ----

#* Return a Plotly Seasonality Plot
#*
#* @param package The package to get download history
#* @param start The start date
#* @param end The end date
#* @param by The aggregation window
#* @param feature The feature to focus on. Set to "auto" by default. Can be one of: "auto", "second", "minute", "hour", "wday.lbl", "week", "month.lbl", "quarter", "year"
#*
#* @get /cran/seasonalityplot
#* @serializer htmlwidget
function(package = "dplyr", start = "2011-01-01", end = lubridate::today(), by = "day", feature = "auto") {

    if (!feature %in% c("auto", "second", "minute", "hour", "wday.lbl", "week", "month.lbl", "quarter", "year")) {
        feature <- "auto"
    }

    data_prepared_tbl <- get_cran_data(package, start, end, by)

    data_prepared_tbl %>%
        group_by(package) %>%
        plot_seasonal_diagnostics(
            date, count,
            .title = str_glue("Package Downloads of: {package}"),
            .feature_set = feature
        )
}
