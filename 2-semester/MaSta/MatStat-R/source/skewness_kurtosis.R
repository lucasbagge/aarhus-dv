# Extra R funktioner til Matematisk Statistik
# (uh, 2019, 2021)
#
# deskriptiv analyse: skewness and kurtosis som defineret i MSRR, 2.7
# simple estimatorer: sample skewness and kurtosis. 
#
# disse estimatorer er ikke unbiased, generelt, men kun asymptotisk unbiased
# der findes faktisk ingen estimatorer for skewness og kurtosis,
# som generelt er unbiased. 
# med generelt mener jeg: uanset hvilken fordeling data stammer fra.
#
# arguments: x: data (numeric vector))
#===================================================================#

# Eksempel: normalfordelte samples. 
# Teoretisk skewness og kurtosis er 0
# 
# prøv gentagene gange:
# skewness(rnorm(10))
# og sammenlingn med
# skewness(rnorm(100))
#
# shortcut for gentagene gange: funktion replicate (læs help doc)
#
# hist(replicate(1000, skewness(rnorm(10))), main = "Estimated skewness, Gaussian, sample size 10")
#
# Hvad synes I om resultatet? Tror I, at skewness estimatoren er biased,
# når vi arbejder med normalfordelte data?
# (ute synes det ser egentligt pænt ud: nogenlunde symmetrisk omkring 0, så 
#   burde middelværdien også være 0 - den sande værdi i tilfælde af normalfordelingen)
#
# det samme for kurtosis:
# hist(replicate(1000, kurtosis(rnorm(10))), main = "Estimated kurtosis, Gaussian, sample size 10")
# hist(replicate(1000, kurtosis(rnorm(100))), main = "Estimated kurtosis, Gaussian, sample size 100")

skewness <- function(x){
  n <- length(x)
  if (n < 1) stop("function skewness: argument x does not contain any data")
  xcentr <- x - mean(x)
  mean(xcentr^3) / sqrt(mean(xcentr^2))^3
}

kurtosis <- function(x){
  n <- length(x)
  if (n < 1) stop("function kurtosis: argument x does not contain any data")
  xcentr <- x - mean(x)
  mean(xcentr^4) / (mean(xcentr^2))^2 - 3
}

