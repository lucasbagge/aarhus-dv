library(mvtnorm)

em_gaussian_mix <- function(dataset, K, max_iter=100, epsilon=1e-3) {
  
  # get the dataset classification given the current indicators
  get_classes <- function(gammak)
    apply(gammak,1,function(row) which.max(row))
  
  d      <- ncol(dataset)                                # number of dimensions
  N      <- nrow(dataset)                                # number of samples
  ranges <- sapply(1:d, function (i) range(dataset[,i])) # the ranges for each dimension
  
  # initial values
  pik <- rep(1/K,K)
  muk <- t(replicate(K, sapply(1:d, function(i) runif(1,ranges[1,i], ranges[2,i]))))
  Sigmas <- array(rep(NA,2*2*3), c(2,2,3))
  
  for (k in 1:K) Sigmas[,,k] <- diag(d)
  
  gammak <- matrix(rep(0, K * N), ncol = K) # the responsabilities
  
  old_gammak <- gammak
  
  # EM steps
  for(it in 1:max_iter) {
    
    # Expectation step: compute responsabilities
    
    for (k in 1:K) {
      gammak[,k] <- apply(dataset, 1,
                          function(xi) {
                            pik[k] * dmvnorm(xi,muk[k,], Sigmas[,,k])
                          })
    }
    gammak <- t(apply(gammak, 1, function(row) row/sum(row)))
    
    if (sum(abs(gammak - old_gammak)) < epsilon) # convergence achieved?
      break
    else
      old_gammak <- gammak
    
    # Maximization step: maximize the expected value wrt parameters theta
    
    Nk  <- sapply(1:K, function (k) sum(gammak[,k]))
    pik <- Nk/N
    for (k in 1:K) {
      muk[k,]     <- apply(gammak[,k] * dataset,2,sum) / Nk[k]
      Sigmas[,,k] <- diag(d) * 0 # reset
      for(n in 1:N) {
        Sigmas[,,k] <- Sigmas[,,k] +
          gammak[n,k]* (dataset[n,]-muk[k,])%*%t(dataset[n,]-muk[k,])
      }
      Sigmas[,,k] <- Sigmas[,,k] / Nk[k]
    }
  }
  
  list(mu = muk, 
       Sigmas = Sigmas, 
       gammak = gammak, 
       pred = get_classes(gammak)
  )
}

test_iris <- iris[1:2] |> data.matrix()
options(scipen = 999)
results_func <- em_gaussian_mix(test_iris, K = 3)

plot(test_iris, col=c("red","green","blue")[results_func$pred],
     xlab="X1", ylab="X2", pch=10)

plot(test_iris,
     col = rgb(results_func$gammak[,1],
               results_func$gammak[,2],
               results_func$gammak[,3]),
     xlab = "X1",
     ylab = "X2",
     pch = 20
)


