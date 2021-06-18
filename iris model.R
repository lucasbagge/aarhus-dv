data(iris)

library(tidyverse)
library(tidymodels)

# initial_split from rsample package which is part of tidymodels
iris_split <- initial_split(iris, prop = 0.7)

# extract training and testing sets
iris_train <- training(iris_split)
iris_test <- testing(iris_split)

iris_recipe <-
  #define your formula
  recipe(Species ~., data = iris) %>%
  # if you are planning to normalize your numerical values
  step_normalize(all_numeric()) %>%
  # if you are planning to knn-ly fill the missing values for categorical type
  step_knnimpute(Species)

iris_train_preprocessed <- iris_recipe %>%
  # apply the recipe to the training data
  prep(iris_train) %>%
  # extract the pre-processed training dataset
  juice()

knn_model <-
  # specify that the model is a k-Nearest Neigbhour (kNN)
  nearest_neighbor() %>%
  # select the package that the model coming from
  set_engine("kknn") %>%
  # choose mode
  set_mode("classification")

library(workflows)
# set the workflow
knn_workflow <- workflow() %>%
  # add the recipe
  add_recipe(iris_recipe) %>%
  # add the model
  add_model(knn_model)

knn_fit <- knn_workflow %>%
  # fit the final best model to the training set and evaluate the test set
  last_fit(iris_split)

# Obtain and format results produced by tuning functions
knn_predictions <- knn_fit %>%
  collect_predictions() %>% 
  

knn_performance <- knn_fit %>%
  collect_metrics()

knn_predictions %>%
  conf_mat(truth = Species, estimate = .pred_class)

final_knnmodel <- fit(knn_workflow, iris)

# https://www.datum.my/post/tidymodels/
