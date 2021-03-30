

########################################################################
# Funktion til indtegning af konfidensintervaller.
# Input er punkter (x,y), og nedre og Ã¸vre endepunkter i 
# konfidensintervaller. Alle vektorer har samme lÃ¦ngde.
#

errorbar=function(x,y,lower,upper){
  points(x,y)
  arrows(x,lower,x,upper,code=3,angle=90,length=0.05)
}



#######################################################################

# Funktion qqnormFlere deler et datasÃ¦t op i grupper og tegner qqplot 
# for hver gruppe i det samme plotvindue.
# Input er en vektor med data (argument x) 
# og en vektor der definerer grupper (argument grupper).
# Funktionen her er identisk med Utes qqnorm_mult, bortset fra 
# at default for qqlines er FALSE, og der er en ekstra instilling "datax"

# De valgfrie argumenter er 
# col: farve for hver gruppe
# pch: symbol for hver gruppe
# xlab: titel hÃ¸rende til aksen med normalfordelingsfraktiler
# ylab: titel hÃ¸rende til akse med data
# datax: hvis data skal vÃ¦re langs fÃ¸rsteaksen
# legend: hvis legend skal tilfÃ¸jes
# qqlines: hvis qqlines skal tilfÃ¸jes

qqnormFlere = function(x, grupper, col = NULL, pch = NULL, 
                       main = "", xlab = "Theoretical Quantiles", ylab = "Sample Quantiles",
                       datax = FALSE, legend = TRUE, qqlines = FALSE){
  # lidt fejlbehandling
  if (missing(x)) stop ("datavektor mangler")
  if (missing(grupper)) stop ("gruppevariabel mangler")
  if (length(x) != length(grupper)) stop ("x og grupper skal have samme lÃ¦ngde")
  # lave grupper om til en faktor
  grupper = factor(grupper)
  # valg af farver og symboler hvis ikke specificeret
  ngrupper = nlevels(grupper)
  if (is.null(col)) col = c(1:ngrupper)
  col = rep(col, length.out = ngrupper)
  if (is.null(pch)) pch = c(1:ngrupper)
  pch = rep(pch, length.out = ngrupper)
  # beregn vÃ¦rdierne i qqplots
  alleqq <- tapply(x, grupper, qqnorm, plot.it = FALSE, datax = datax)
  xrange <- range(sapply(alleqq, function(res) range(res$x)))
  yrange <- range(sapply(alleqq, function(res) range(res$y)))
  if (datax) {xlab1=ylab; ylab=xlab; xlab=xlab1}
  plot(xrange, yrange, type="n", xlab = xlab, ylab = ylab, main = main)
  for (i in seq_along(alleqq)) {
    points(alleqq[[i]], col = col[i], pch = pch[i])
    if (qqlines){
      if (datax) {
        qqline(alleqq[[i]]$x,col=col[i],datax=TRUE)
      } else {
        qqline(alleqq[[i]]$y, col = col[i])
      }
    }
  }
  if(legend) legend("topleft", legend = names(alleqq), col = col, pch = pch)
}



########################################################################

# Funktion der beregner konfidensinterval for ukendte vÃ¦rdi 
# af forklarende variabel i regressionsmodel. Input er 
# output fra kaldet lm(x~t) og nye mÃ¥linger y.

inversReg=function(lmUD,y){
  sumUD=summary(lmUD)
  xbar=mean(lmUD$model[,1])
  m=length(y)
  ybar=mean(y)
  t0=qt(0.975,sumUD$df[2])
  ahat=sumUD$coefficients[1,1]
  bhat=sumUD$coefficients[2,1]
  s2r=(sumUD$sigma)^2
  SSDt=s2r/(sumUD$coefficients[2,2])^2
  A=bhat^2-t0^2*s2r/SSDt
  if (A>0){
    B=-2*t0^2*s2r*(ybar-xbar)/(bhat*SSDt)
    C=-t0^2*s2r*(1/m+1/(sumUD$df[2]+2)+(ybar-xbar)^2/(bhat^2*SSDt))
    thetahat=(ybar-ahat)/bhat
    ci=thetahat+(-B+c(-1,1)*sqrt(B^2-4*A*C))/(2*A)
    return(list(estimat=thetahat,konfidensinterval=ci))
  } else {
    return("Problem er ikke veldefineret da beta kan vÃ¦re nul")
  }
}


#######################################################################

# Funktionen additivitetsPlot beregner gennemsnit i hver gruppe 
# defineret ved A:B (A og B er faktorer) og afsÃ¦tter disse mod A.
# For hvert niveau af B forbindes gennemsnit. 
# Desuden angives plus minus standard error for gennemsnittet.

additivitetsPlot=function(A,B,x){
  nlevB=length(levels(B))
  NavnA <-deparse(substitute(A))
  NavnB <-deparse(substitute(B))
  interaction.plot(A,B,x,ylim=range(x),col=c(1:nlevB),fixed=TRUE,
                   xlab=NavnA,trace.label=NavnB,ylab="Gennemsnit")
  me=aggregate(x,list(A:B),mean)
  sdv=aggregate(x,list(A:B),sd)
  n=aggregate(x,list(A:B),length)
  lower=me[,2]-sdv[,2]/sqrt(n[,2])
  upper=me[,2]+sdv[,2]/sqrt(n[,2])
  levA=levels(A)
  nlevA=length(levA)
  for (i in 1:nlevB){
    med=(c(1:nlevA)-1)*nlevB+i
    arrows(c(1:nlevA),lower[med],c(1:nlevA),upper[med],
           code=3,angle=90,length=0.05,col=i)
  }
}

########################################################################

# Funktionen FWstep finder den nÃ¦ste variabel, som inkluderes i 
# forward selection i en multipel regressionsmodel.
# Input er en matrix med vÃ¦rdierne af de forklarende variable, 
# en vektor x med respons og en vektor "med", der indeholder 
# sÃ¸jlenumrene pÃ¥ de forklarende variable, der allerede er inkluderet.

FWstep=function(T,x,med=c()){
  d=dim(T)[2]; n=length(x)
  ma=ls.diag(lsfit(T[,1],x))$std.dev
  res=rep(ma,d)
  if (length(med)==0){lookup=c(1:d)} else {lookup=c(1:d)[-med]}
  for (i in lookup){
    med1=c(med,i)
    res[i]=ls.diag(lsfit(T[,med1],x))$std.dev
  }
  sny=min(res)
  medny=which.min(res)
  med1=c(med,medny)
  ud=lsfit(T[,med1],x)
  uddiag=ls.diag(ud)
  betahat=ud$coef
  sds=uddiag$std.err
  pval=2*pt(-abs(betahat/sds),n-1-length(med1))
  return(list(sny=sny,med=med1,pval=pval))
}


########################################################################

# Funktionen FWcrossval laver leave one out crossvalidation for forward 
# selektion i en multipel regressionsmodel.
# Input er en matrix med vÃ¦rdierne af de forklarende variable, 
# en vektor x med respons og et antal k, der siger hvor mange led 
# der skal medtages i forward selektion.

FWcrossval=function(T,x,k){
  d=dim(T)[2]
  n=length(x)
  Mr=matrix(0,n,k)
  for (i in 1:n){
    T0=T[-i,]
    x0=x[-i]
    res=rep(0,d)
    for (j in 1:d){
      res[j]=summary(lm(x0~T0[,j]))$sigma
    }
    med=which.min(res)
    beta=lsfit(T0[,med],x0)$coef
    Mr[i,1]=(x[i]-sum(beta*c(1,T[i,med])))^2
    if (k>1){
      for (j in 2:k){
        res=rep(10,d)
        for (r in c(1:d)[-med]){
          med1=c(med,r)
          res[r]=ls.diag(lsfit(T0[,med1],x0))$std.dev
        }
        med=c(med,which.min(res))
        beta=lsfit(T0[,med],x0)$coef
        Mr[i,j]=(x[i]-sum(beta*c(1,T[i,med])))^2  
      }}
  }
  return(sqrt(apply(Mr,2,sum)/n))
}


########################################################################
