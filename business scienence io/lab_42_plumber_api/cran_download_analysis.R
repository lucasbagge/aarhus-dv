# LAB 42: PLUMBER API ----
# CRANLOGS ANALYSIS ----

# 1.0 LIBRARIES ----

library(tidyverse)
library(timetk)
library(cranlogs)

# 2.0 GET DOWNLOADS ----

pkg <- c("dplyr")

pkg_downloads_raw <- cran_downloads(pkg, from = "2011-01-01")

pkg_downloads_tbl <- as_tibble(pkg_downloads_raw)
pkg_downloads_tbl

# 3.0 VISUALIZATIONS ----

# * Time Plot ----
pkg_downloads_tbl %>%
    group_by(package) %>%
    filter_by_time(.end_date = "2020-07") %>%
    summarise_by_time(date, .by = "week", count = sum(count)) %>%
    plot_time_series(date, count,
                     .facet_ncol = 2, .smooth_period = 365,
                     .title = "Monthly Downloads of R Packages")

# * Seasonality Plot ----

features <- "month.lbl"

pkg_downloads_tbl %>%
    plot_seasonal_diagnostics(
        date, count, .feature_set = features
    )


