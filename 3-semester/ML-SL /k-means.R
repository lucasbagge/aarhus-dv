library(tibble)
library(purrr)
library(ggplot2)
library(dplyr)

## k-means function ----
k_means <- function(dataset, K, max_iter=100) {
  
  get_classes <- function(rnk) apply(rnk,1,function(row) which.max(row))
  
  d      <- ncol(dataset)                                # number of dimensions
  N      <- nrow(dataset)                                # number of samples
  n      <- nrow(dataset)
  
  ranges <- 
    map(1:d, function(i) range(dataset[,i])) |>
    as.data.frame() |>
    as.matrix() 
  
  mu <- 
    replicate(K,
              map_dbl(1:d, 
                      function(i) runif(1, ranges[1,i] , ranges[2,i]))
    ) |> 
    t()
  
  rnk <- matrix(rep(0,K*n), ncol=K)
  old_classes <- get_classes(rnk)
  
  for(it in 1:max_iter) {
    
    for(n in 1:N) {
      distances <- map_dbl(1:K, 
                           function(k) norm(as.matrix(test_iris[n,] - mu[k,]),
                                            "F"))
      rnk[n,]   <- rep(0,K)
      rnk[n,which.min(distances)] <- 1
    }
    
    classes <- get_classes(rnk)
    if (all(old_classes == classes))
      break
    else 
      old_classes <- classes
    
    for(k in 1:K) {
      mu[k,]  <- rnk[,k] %*% dataset / sum(rnk[,k])
    }
  }
  
  list(mu=mu, pred=classes)
}

test_iris <- iris[1:2] |> data.matrix()

results_func <- k_means(test_iris, K = 3)

# Visual ----
test_iris |> 
  as_tibble() |> 
  janitor::clean_names() |> 
  dplyr::bind_cols(results_func$pred |> as_tibble()) |> 
  ggplot(aes(x = sepal_length, 
             y = sepal_width)) +
  geom_point(
    mapping = aes(shape =  as.character(value),
                  color = as.character(value))) +
  geom_point(
    data = results_func$mu |> 
      as_tibble() |> 
      janitor::clean_names(), 
    aes(v1, v2, size = 5)
  ) +
  theme_light()
