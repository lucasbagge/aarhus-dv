# LEARNING LAB 41: METAFLOW ----
# Module: Metaflow Installation Instructions ----

# 1.0 Windows Support ----
# - https://docs.metaflow.org/v/r/getting-started/install#windows-support
# - Use Windows Subsystem for Linux (WSL)

# 2.0 Installation -----

# Installs Metaflow for R
devtools::install_github("Netflix/metaflow", subdir="R")

# Installs Metaflow for Python
reticulate::conda_list()

reticulate::conda_create(
    envname  = "metaflow-test",
    packages = c("metaflow", "pandas", "numpy")
)

# Connects Metaflow R to Metaflpw Python
reticulate::use_condaenv("metaflow-test", required = TRUE)

# 3.0 TEST ----

metaflow::test()


# 4.0 Metaflow Command Line ----

# In Termiinal:
# conda env list
# conda activate /Users/mdancho/Library/r-miniconda/envs/metaflow-test
# metaflow configure reset

