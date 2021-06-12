# MWait.R: R kode til Eksamen Matematisk Statistik, F 2021.
#
# Funktion rmeanwait: 
#    simulation af stikprøvegennemsnit fra ventetidsfordelingen i opgave 1.
#
# Argumenter: 
#    n = antal simulerede stikprøver, 
#    size = stikprøvestørrelse, (kaldes m i opgave 1) 
#    theta = fordelingsparameter. Default værdi: theta = 1.
# Eksempel:
#   rmeanwait(3, 5, 8)
# simulerer 3 stikprøver af størrelse 5 fra ventetidsfordelingen 
# med theta = 8 og returnerer de 3 stikprøvegennemsnit 

rmeanwait <- function(n, size = 1, theta = 1) {
  replicate(n, theta * mean(-log(1 - sqrt(runif(size)))))
}