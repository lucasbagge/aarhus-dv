FROM mdancho/h2o-verse:3.30.0.1

# install the linux libraries needed for plumber
RUN apt-get update -qq && apt-get install -y \
  libssl-dev \
  libcurl4-gnutls-dev

## Install R Packages
RUN install2.r --error --deps TRUE \
    cranlogs \
    plumber

# copy everything from the current directory into the container
COPY / /

# open port 8000 to traffic
EXPOSE 8000

# When the container starts, start the main.R script
ENTRYPOINT ["Rscript", "main.R"]



###### INSTRUCTIONS ######

# 1. Create Image:
# sudo docker build . -t mdancho/h2o-plumber

# 2. Run Image Locally
# docker run --rm -p 8000:8000 mdancho/h2o-plumber

# 3. Test Your API
# http://localhost:8000/cran?package=tidyquant&start=2017-01-01
# http://localhost:8000/cran/timeplot?package=tidyquant&start=2017-01-01
# http://localhost:8000/cran/seasonalityplot?package=tidyquant&start=2017-01-01&feature=month.lbl

# 4. Shutdown
# Ctrl + C
