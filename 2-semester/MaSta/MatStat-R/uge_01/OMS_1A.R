# Source code til opgave 1B fra opgavesamlingen til Matematisk Statistik 2021
#
# Du må godt tilpasse navn og dato :-)
#'---
#' title: "Opgave 1B"
#' author: "Ute Hahn"
#' date: "30. Januar 2021"
#'---
#'
#'Vi vil først lave en lille simulationsstudie: Vi generer 1000 normalfordelte
#'tal og tegner en histogram. Beregner også gennemsnittet og median, og indtegner den.
#'

# gemmer tallene i variablen x

x <- rnorm(1000)

# beregner medianen, og gemmer resultaterne under navnet x_med

x_med <- median(x)

# plotter histogram

hist(x)

#tilfojer en grøn vertikal linje gennem medianen

abline(v = x_med, col = "green")

#============== Lav det selv opgave ===============
# 
# I roxygen kommentarer nedenunder ser du eksempler til brug af RMarkdown 
# til overskrifter og bullet lists.
# Find forklaring under Help > Markdown Quick Reference 

#'## Opgaven: ny simulationsstudie
#'* Simuler 2000 realiseringer fra standard normalfordelingen.
#'* Plot histogrammet og integn en blå vertikal linie for gennemsnittet.
#'* Under plottet, beskriv kort om du ser forskelle mellem de to histogrammer.