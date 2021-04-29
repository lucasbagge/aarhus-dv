library(tidyverse)   # Loads dplyr, ggplot2, purrr, and other useful packages
library(tidymodels)  # Loads parsnip, rsample, recipes, yardstick
library(skimr)       # Quickly get a sense of data
library(knitr) 
library(discrim)

telco <- 
  read_csv("https://raw.githubusercontent.com/DiegoUsaiUK/Classification_Churn_with_Parsnip/master/00_Data/WA_Fn-UseC_-Telco-Customer-Churn.csv") %>% 
  na.omit() %>% 
  select(-customerID) %>% 
  mutate(Churn = as.factor(Churn))

telco %>% 
  skimr::skim()

set.seed(seed = 1972) 
train_test_split <-
  initial_split(
    data = telco,     
    prop = 0.80   
  ) 

train_test_split

train_tbl <- train_test_split %>% training() 
test_tbl  <- train_test_split %>% testing() 

rand_model <-
  rand_forest() %>%
  set_engine(engine = "ranger") %>%
  set_mode("classification")

nb_model <- 
  naive_Bayes() %>%
  set_mode("classification") %>%
  set_engine("naivebayes")

rec <- 
  recipe(Churn ~ ., data = train_tbl) %>%
  step_dummy(all_nominal(), -all_outcomes()) %>%
  step_normalize(all_numeric())

rec %>% prep() %>% juice()

wf <- 
  workflow() %>% 
  add_model(rand_model) %>% 
  add_recipe(recipe = rec)

wf_nb <- 
  workflow() %>% 
  add_model(nb_model) %>% 
  add_recipe(recipe = rec)

fit <- 
  wf %>% 
  fit(data = train_tbl)

fit_nb <- 
  wf_nb %>% 
  fit(data = train_tbl)

fit %>% 
  pull_workflow_fit()  

fit_nb %>% 
  pull_workflow_fit()  
  
pred <- predict(fit, test_tbl, type = "prob") %>% 
  bind_cols(test_tbl %>% select(gender, Churn)) 

pred_bayes <- 
  predict(fit_nb, test_tbl, type = "prob") %>% 
  bind_cols(test_tbl %>% select(gender, Churn)) 

pred %>% 
  roc_curve(truth = as.factor(Churn), .pred_No) %>% 
  autoplot()

pred %>% 
  roc_auc(truth = as.factor(Churn), .pred_No)

pred_bayes %>% 
  roc_auc(truth = as.factor(Churn), .pred_No)
  