install_dependencies <- function() {
    if (!suppressMessages(require(tidymodels))) {
        install.packages("tidymodels", repos = "https://cloud.r-project.org", quiet=TRUE)
    }
    if (!suppressMessages(require(modeltime))) {
        install.packages("modeltime", repos = "https://cloud.r-project.org", quiet=TRUE)
    }
    if (!suppressMessages(require(timetk))) {
        install.packages("timetk", repos = "https://cloud.r-project.org", quiet=TRUE)
    }
    if (!suppressMessages(require(glmnet))) {
        install.packages("glmnet", repos = "https://cloud.r-project.org", quiet=TRUE)
    }
    if (!suppressMessages(require(lubridate))) {
        install.packages("lubridate", repos = "https://cloud.r-project.org", quiet=TRUE)
    }
    if (!suppressMessages(require(tidyverse))) {
        install.packages("tidyverse", repos = "https://cloud.r-project.org", quiet=TRUE)
    }
}
