FROM rocker/verse:latest

## Install debian packages
RUN apt-get update -qq && apt-get -y --no-install-recommends install \

    # usethis dependencies
    build-essential \
    libcurl4-gnutls-dev \
    libxml2-dev \
    libssl-dev \

    # sf dependencies
    lbzip2 \
    libfftw3-dev \
    libgdal-dev \
    libgeos-dev \
    libgsl0-dev \
    libgl1-mesa-dev \
    libglu1-mesa-dev \
    libhdf4-alt-dev \
    libhdf5-dev \
    libjq-dev \
    liblwgeom-dev \
    libpq-dev \
    libproj-dev \
    libprotobuf-dev \
    libnetcdf-dev \
    libsqlite3-dev \
    libssl-dev \
    libudunits2-dev \
    netcdf-bin \
    postgis \
    protobuf-compiler \
    sqlite3 \
    tk-dev \
    unixodbc-dev \

    # h2o dependencies
    libxml2-dev \
    libcairo2-dev \
    libsqlite3-dev \
    libmariadbd-dev \
    libpq-dev \
    libssh2-1-dev \
    unixodbc-dev \
#    libcurl4-openssl-dev \
    libssl-dev \

    # rstan dependencies
    libnlopt-dev



## Get Java (for h2o R package)
RUN apt-get update -qq \
    && apt-get -y --no-install-recommends install \
        cmake \
        default-jdk \
        default-jre \
    && R CMD javareconf

## Install R Packages
RUN install2.r --error --deps TRUE \
    usethis \
    tidyquant \
    plotly \
    embed


RUN R -e "devtools::install_version('h2o', version = '3.30.0.1', dependencies = TRUE)"
