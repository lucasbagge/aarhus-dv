# Extra R funktioner til Matematisk Statistik
# (uh, 2019, 2021)
#
# deskriptiv analyse: qq plot og qqline (se MSRR, 2.4)
#
# Her får I en funktion der laver simultan qq-plot når data
# stammer fra flere grupper
# Valgtfrit kan der tilføjes en qqline til hver gruppe
#===================================================================#

# meaning of arguments:
# y:       data vector
# groups:  a vector with group assignment
# col:     colours, one for each group. If NULL, take R colors from 1 to number of groups
# pch:     plot character, one for each group, as col.
# main:    title, xlab, ylab: labels of x- and y-axis
# ...:     further plot parameters, for example line type (lty) or line thickness (lwd)
# legend:  if a legend should be added, set to TRUE
# qqlines: if qqlines should be added, set to TRUE.

# # eksempel:
# # fake højde af 20 mænd og kvinder
# 
# hojde_m <- rnorm(20, mean = 180, sd = 8)
# hojde_k <- rnorm(20, mean = 167, sd = 7)
# hojde <- c(hojde_k, hojde_m)
# 
# # lav gruppe variable, faktor
# koen_char <- c(rep("K", 20), rep("M", 20))
# koen <- as.factor(koen_char)
# 
# # forskelligt pyntede plots:
# qqnorm_multi(hojde, koen)
# qqnorm_multi(hojde, koen, pch = c(21,16), qqlines = FALSE, 
#              main = "normal qq plot without qqlines")
# qqnorm_multi(hojde, koen, col = c("red", "blue"), pch = 21, lty = "dashed")

qqnorm_multi <- function(y, groups, col = NULL, pch = NULL, 
   main = "", xlab = "Theoretical Quantiles", ylab = "Sample Quantiles",
                           ..., legend = TRUE, qqlines = TRUE){
  # lidt fejlbehandling
  if (missing(y)) stop ("no data given")
  if (missing(groups)) stop ("no groups given")
  if (length(y) != length(groups)) stop ("y and groups need to be vectors of same length")
  
  # lav en faktor variabel, hvis ikke groups allerede er det
  groups = factor(groups)
  # valg farver og symboler hvis de mangler
  ngroups <- nlevels(groups)
  if (is.null(col)) col <- 1 : ngroups
  col <- rep(col, length.out = ngroups)
  if (is.null(pch)) pch <- 1 : ngroups
  pch <- rep(pch, length.out = ngroups)
  # beregn værdier
  allqq <- tapply(y, groups, qqnorm, plot.it = FALSE)
  xrange <- range(sapply(allqq, function(res) range(res$x)))
  yrange <- range(sapply(allqq, function(res) range(res$y)))
  plot(xrange, yrange, type="n", xlab = xlab, ylab = ylab, main = main)
  for (i in seq_along(allqq)) {
    points(allqq[[i]], col = col[i], pch = pch[i], ...)
    if (qqlines) qqline(allqq[[i]]$y, col = col[i], ...)
  }
  if(legend) legend("topleft", legend = names(allqq), col = col, pch = pch)
}