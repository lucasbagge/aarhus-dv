######################################################
# Machine Trading Analysis with R                    #
# (c) Diego Fernandez Garcia 2015-2017               #
# www.exfinsis.com                                   #
######################################################

# 1. Machine Trading Analysis Data

# 1.1. Load R packages 
library("caret")
library("corrplot")
library("forecast")
library("kernlab")
library("neuralnet")
library("PerformanceAnalytics")
library("quantmod")
library("tseries")
library(tidymodels)
library(tidyverse)
library(tidyquant)
library("xgboost")

# 1.2. Data Downloading or Reading

# 1.2.1. Yahoo Finance
getSymbols(Symbols="SPY",src="yahoo",from="2007-01-01",to="2017-01-01")
spy <- SPY$SPY.Adjusted
spy %>% head()
# 1.2.2. Data Reading
# data <- read.csv("Machine-Trading-Analysis-Data.txt",header=T)
#spy <- xts(data[,2],order.by=as.Date(data[,1]))
spy_tiblle <- tq_get("SPY",get = "stock.prices",from="2007-01-01",to="2017-01-01") %>% 
  tq_mutate(select = adjusted, dailyReturn, type = "log") %>% 
  tq_mutate(select = daily.returns, Lag, k = 1:9) %>% 
  select(date, daily.returns, starts_with("Lag")) %>% 
  na.omit()
spy_tiblle %>% head()
# 2. Feature Creation

# 2.1. Target Feature
rspy <- dailyReturn(spy,type="log")
rspy %>% head()
# 2.2. Predictor Features
rspy1 <- Lag(rspy,k=1)
rspy1 %>% head()
rspy2 <- Lag(rspy,k=2)
rspy3 <- Lag(rspy,k=3)
rspy4 <- Lag(rspy,k=4)
rspy5 <- Lag(rspy,k=5)
rspy6 <- Lag(rspy,k=6)
rspy7 <- Lag(rspy,k=7)
rspy8 <- Lag(rspy,k=8)
rspy9 <- Lag(rspy,k=9)

# 2.3. All Features
rspyall <- cbind(rspy,rspy1,rspy2,rspy3,rspy4,rspy5,rspy6,rspy7,rspy8,rspy9)
colnames(rspyall) <- c("rspy","rspy1","rspy2","rspy3","rspy4","rspy5","rspy6","rspy7","rspy8","rspy9")
rspyall <- rspyall[complete.cases(rspyall),]
rspyall %>% head()
# 3. Range Delimiting

# 3.1. Training Range
rspyt <- window(rspyall, end = "2014-01-01")
rspyt %>% tail()
rspyt %>% head()
library(timetk)
rspyt_tibble <- spy_tiblle %>%
  filter(date <= "2014-01-01")
rspyt_tibble %>% tail()
# 3.2. Testing Range

rspyf <- window(rspyall,start="2014-01-01",end="2016-01-01")
rspyf %>% head()
rspyf %>% tail()
rspyf_tibble <- spy_tiblle %>%
  filter(date >=  "2014-01-01" & date <= "2016-01-01")
rspyf_tibble %>% head()
rspyf_tibble %>% tail()

# 3.3. Intermediate Testing Range 
# Same length as Training Range
rspyp <- window(rspyall,start="2009-01-15",end="2016-01-01")
length(rspyt)
length(rspyp)

rspyp_tibble <- spy_tiblle %>% 
  filter(date >=  "2009-01-15" & date <= "2016-01-01")
  
nrow(rspyt_tibble)
nrow(rspyp_tibble)

# 3.4. Trading Range
rspys <- window(rspyall,start="2016-01-01")

# 3.5. Intermediate Trading Range
# Same length as Training Range
rspyi <- window(rspyall,start="2010-01-15")
length(rspyt)
length(rspyi)

# 4. Predictor Features Selection

# 4.2. Predictor Features Linear Regression
lmta <- lm(rspy~rspy1+rspy2+rspy3+rspy4+rspy5+rspy6+rspy7+rspy8+rspy9,data=rspyt)
summary(lmta)
lmtb <- lm(rspy~rspy1+rspy2+rspy5,data=rspyt)
summary(lmtb)
# Clear Plots area before running code
par(mfrow=c(1,2))
plot(coredata(rspyt$rspy1),coredata(rspyt$rspy),xlab="rspy1t",ylab="rspyt")
abline(lm(rspyt$rspy~rspyt$rspy1),col="red")
plot(coredata(rspyt$rspy2),coredata(rspyt$rspy),xlab="rspy2t",ylab="rspyt")
abline(lm(rspyt$rspy~rspyt$rspy2),col="red")
plot(coredata(rspyt$rspy5),coredata(rspyt$rspy),xlab="rspy5t",ylab="rspyt")
abline(lm(rspyt$rspy~rspyt$rspy5),col="red")
par(mfrow=c(1,1))

# 4.2. Predictor Features Correlation
crspyt <- round(cor(rspyt[,2:10]),2)
crspyt
corrplot(crspyt,type="lower")

# 4.3. Predictor Features Selection Filter Methods

# 4.3.1. Univariate Filters
sbfctrlt <- sbfControl(functions=lmSBF)
sbft <- sbf(rspy~rspy1+rspy2+rspy3+rspy4+rspy5+rspy6+rspy7+rspy8+rspy9,data=rspyt,sbfControl=sbfctrlt)
sbft

# 4.4. Predictor Features Selection Wrapper Methods

# 4.4.1. Recursive Feature Elimination
rfectrlt <- rfeControl(functions=lmFuncs)
rfet <- rfe(rspy~rspy1+rspy2+rspy3+rspy4+rspy5+rspy6+rspy7+rspy8+rspy9,data=rspyt,rfeControl=rfectrlt)
rfet

# 4.5. Predictor Features Selection Embedded Methods
lassot <- train(rspy~rspy1+rspy2+rspy3+rspy4+rspy5+rspy6+rspy7+rspy8+rspy9,data=rspyt,method="lasso")
predictors(lassot)

# 4.6. Predictor Features Extraction

# 4.6.1. Principal Component Analysis
pcat <- princomp(rspyt[,2:10])
summary(pcat)
plot(pcat)

# 5. Algorithm Training and Testing

# 5.1. Ensemble Methods

# eXtreme Gradient Boosting Machine Regression

# 5.1.1. eXtreme Gradient Boosting Regression training
xgbmta <- train(rspy~rspy1+rspy2+rspy5,data=rspyt,method="xgbTree")
xgbmtb <- train(rspy~rspy1+rspy2+rspy3+rspy4+rspy5+rspy6+rspy7+rspy8+rspy9,data=rspyt,method="xgbTree",preProcess="pca")

# eXtreme Gradient Boosting Regression optimal training parameters
xgbmta$bestTune
plot(xgbmta)
xgbmtb$bestTune
plot(xgbmtb)

# eXtreme Gradient Boosting Regression training results
xgbmta$results
xgbmtb$results

# 5.1.2. eXtreme Gradient Boosting Regression testing
# Intermediate testing step as newdata needs to be same length as training range 
xgbmpa <- predict.train(xgbmta,newdata=rspyp)
xgbmpb <- predict.train(xgbmtb,newdata=rspyp)

# Limited to testing range
xgbmdfa <- cbind(index(rspyp),as.data.frame(xgbmpa))
xgbmla <- xts(xgbmdfa[,2],order.by=as.Date(xgbmdfa[,1]))
xgbmfa <- window(xgbmla,start="2014-01-01")
xgbmdfb <- cbind(index(rspyp),as.data.frame(xgbmpb))
xgbmlb <- xts(xgbmdfb[,2],order.by=as.Date(xgbmdfb[,1]))
xgbmfb <- window(xgbmlb,start="2014-01-01")

# 5.1.3. eXtreme Gradient Boosting Regression testing chart
plot(rspyf[,1],type="l",main="eXtreme Gradient Boosting Regression A Testing Chart")
lines(xgbmfa,col="blue")
plot(rspyf[,1],type="l",main="eXtreme Gradient Boosting Regression B Testing Chart")
lines(xgbmfb,col="green")

# 5.1.4. eXtreme Gradient Boosting Regression forecasting accuracy
# Convert xts to ts for accuracy function
xgbmftsa <- ts(coredata(xgbmfa),frequency=252,start=c(2014,1))
xgbmftsb <- ts(coredata(xgbmfb),frequency=252,start=c(2014,1))
rspyfts <- ts(coredata(rspyf[,1]),frequency=252,start=c(2014,1))
rspy1fts <- ts(coredata(rspyf[,2]),frequency=252,start=c(2014,1))
accuracy(xgbmftsa,rspyfts)
rndmape <- accuracy(rspyfts,rspy1fts)[5]
xgbmmasea <- accuracy(xgbmftsa,rspyfts)[5]/rndmape
xgbmmasea
accuracy(xgbmftsb,rspyfts)
xgbmmaseb <- accuracy(xgbmftsb,rspyfts)[5]/rndmape
xgbmmaseb

# 5.2. Algorithm Training Optimal Parameters Selection Control

# 5.2.1. Time Series Cross-Validation
tsctrlt <- trainControl(method="timeslice",initialWindow=168,horizon=82,fixedWindow=TRUE)

# 5.3. Maximum Margin Methods

# Support Vector Machine Regression with Radial Basis Function Kernel

# 5.3.1. RBF Support Vector Machine Regression training
rsvmta <- train(rspy~rspy1+rspy2+rspy5,data=rspyt,method="svmRadial",trControl=tsctrlt)
rsvmtb <- train(rspy~rspy1+rspy2+rspy3+rspy4+rspy5+rspy6+rspy7+rspy8+rspy9,data=rspyt,method="svmRadial",preProcess="pca",trControl=tsctrlt)

# RBF Support Vector Machine Regression optimal training parameters
rsvmta$bestTune
plot(rsvmta)
rsvmtb$bestTune
plot(rsvmtb)

# RBF Support Vector Machine Regression training results
rsvmta$results
rsvmtb$results

# 5.3.2. RBF Support Vector Machine Regression testing
# Intermediate testing step as newdata needs to be same length as training range 
rsvmpa <- predict.train(rsvmta,newdata=rspyp)
rsvmpb <- predict.train(rsvmtb,newdata=rspyp)

# Limited to testing range
rsvmdfa <- cbind(index(rspyp),as.data.frame(rsvmpa))
rsvmla <- xts(rsvmdfa[,2],order.by=as.Date(rsvmdfa[,1]))
rsvmfa <- window(rsvmla,start="2014-01-01")
rsvmdfb <- cbind(index(rspyp),as.data.frame(rsvmpb))
rsvmlb <- xts(rsvmdfb[,2],order.by=as.Date(rsvmdfb[,1]))
rsvmfb <- window(rsvmlb,start="2014-01-01")

# 5.3.3. RBF Support Vector Machine Regression testing chart
plot(rspyf[,1],type="l",main="RBF Support Vector Machine Regression A Testing Chart")
lines(rsvmfa,col="blue")
plot(rspyf[,1],type="l",main="RBF Support Vector Machine Regression B Testing Chart")
lines(rsvmfb,col="green")

# 5.3.4. RBF Support Vector Machine Regression forecasting accuracy
# Convert xts to ts for accuracy function
rsvmftsa <- ts(coredata(rsvmfa),frequency=252,start=c(2014,1))
accuracy(rsvmftsa,rspyfts)
rsvmmasea <- accuracy(rsvmftsa,rspyfts)[5]/rndmape
rsvmmasea
rsvmftsb <- ts(coredata(rsvmfb),frequency=252,start=c(2014,1))
accuracy(rsvmftsb,rspyfts)
rsvmmaseb <- accuracy(rsvmftsb,rspyfts)[5]/rndmape
rsvmmaseb

# 5.4. Multi-Layer Perceptron Methods

# Artificial Neural Network Regression 

# 5.4.1. Artificial Neural Network Regression training
annta <- train(rspy~rspy1+rspy2+rspy5,data=rspyt,method="neuralnet",trControl=tsctrlt)
anntb <- train(rspy~rspy1+rspy2+rspy3+rspy4+rspy5+rspy6+rspy7+rspy8+rspy9,data=rspyt,method="neuralnet",preProcess="pca",trControl=tsctrlt)

# Artificial Neural Network Regression optimal training parameters
annta$bestTune
plot(annta)
anntb$bestTune
plot(anntb)

# Artificial Neural Network Regression training results
annta$results
anntb$results

# 5.4.2. Artificial Neural Network Regression testing
# Intermediate testing step as newdata needs to be same length as training range 
annpa <- predict.train(annta,newdata=rspyp)
annpb <- predict.train(anntb,newdata=rspyp)

# Limited to testing range
anndfa <- cbind(index(rspyp),as.data.frame(annpa))
annla <- xts(anndfa[,2],order.by=as.Date(anndfa[,1]))
annfa <- window(annla,start="2014-01-01")
anndfb <- cbind(index(rspyp),as.data.frame(annpb))
annlb <- xts(anndfb[,2],order.by=as.Date(anndfb[,1]))
annfb <- window(annlb,start="2014-01-01")

# 5.4.3. Artificial Neural Network Regression testing chart
plot(rspyf[,1],type="l",main="Artificial Neural Network Regression A Testing Chart")
lines(annfa,col="blue")
plot(rspyf[,1],type="l",main="Artificial Neural Network Regression B Testing Chart")
lines(annfb,col="green")

# 5.4.4. Artificial Neural Network Regression forecasting accuracy
# Convert xts to ts for accuracy function
annftsa <- ts(coredata(annfa),frequency=252,start=c(2014,1))
accuracy(annftsa,rspyfts)
annmasea <- accuracy(annftsa,rspyfts)[5]/rndmape
annmasea
annftsb <- ts(coredata(annfb),frequency=252,start=c(2014,1))
accuracy(annftsb,rspyfts)
annmaseb <- accuracy(annftsb,rspyfts)[5]/rndmape
annmaseb

# 5.6. Algorithm Testing Accuracy Comparison
accuracy(xgbmftsb,rspyfts)
accuracy(rsvmftsa,rspyfts)
accuracy(annftsa,rspyfts)
xgbmmaseb
rsvmmasea
annmasea

# 6. Machine Trading Strategies

# 6.1. Ensemble Method Trading Strategy

# 6.1.1. eXtreme Gradient Boosting Regression forecasting
# Intermediate forecasting step as newdata needs to be same length as training range 
xgbmi <- predict.train(xgbmtb,newdata=rspyi)

# Limited to trading range
xgbmdfi <- cbind(index(rspyi),as.data.frame(xgbmi))
xgbmli <- xts(xgbmdfi[,2],order.by=as.Date(xgbmdfi[,1]))
xgbms <- window(xgbmli,start="2016-01-01")

# 6.1.2. eXtreme Gradient Boosting Regression trading signals
xgbmsig <- Lag(ifelse(Lag(xgbms)<0&xgbms>0,1,ifelse(Lag(xgbms)>0&xgbms<0,-1,0)))
xgbmsig[is.na(xgbmsig)] <- 0

# 6.1.3. eXtreme Gradient Boosting Regression trading positions
xgbmpos <- ifelse(xgbmsig>1,1,0)
for(i in 1:length(xgbmpos)){xgbmpos[i] <- ifelse(xgbmsig[i]==1,1,ifelse(xgbmsig[i]==-1,0,xgbmpos[i-1]))}
xgbmpos[is.na(xgbmpos)] <- 0
xgbmtr <- cbind(xgbms,xgbmsig,xgbmpos)
colnames(xgbmtr) <- c("xgbms","xgbmsig","xgbmpos")
View(xgbmtr)

# 6.2. Maximum Margin Method Trading Strategy

# 6.2.1. RBF Support Vector Machine Regression forecasting
# Intermediate forecasting step as newdata needs to be same length as training range 
rsvmi <- predict.train(rsvmta,newdata=rspyi)

# Limited to trading range
rsvmdfi <- cbind(index(rspyi),as.data.frame(rsvmi))
rsvmli <- xts(rsvmdfi[,2],order.by=as.Date(rsvmdfi[,1]))
rsvms <- window(rsvmli,start="2016-01-01")

# 6.2.2. RBF Support Vector Machine Regression trading signals
rsvmsig <- Lag(ifelse(Lag(rsvms)<0&rsvms>0,1,ifelse(Lag(rsvms)>0&rsvms<0,-1,0)))
rsvmsig[is.na(rsvmsig)] <- 0

# 6.2.3. RBF Support Vector Machine Regression trading positions
rsvmpos <- ifelse(rsvmsig>1,1,0)
for(i in 1:length(rsvmpos)){rsvmpos[i] <- ifelse(rsvmsig[i]==1,1,ifelse(rsvmsig[i]==-1,0,rsvmpos[i-1]))}
rsvmpos[is.na(rsvmpos)] <- 0
rsvmtr <- cbind(rsvms,rsvmsig,rsvmpos)
colnames(rsvmtr) <- c("rsvms","rsvmsig","rsvmpos")
View(rsvmtr)

# 6.3. Multi-Layer Perceptron Method Trading Strategy

# 6.3.1. Artificial Neural Network Regression forecasting
# Intermediate forecasting step as newdata needs to be same length as training range 
anni <- predict.train(annta,newdata=rspyi)

# Limited to trading range
anndfi <- cbind(index(rspyi),as.data.frame(anni))
annli <- xts(anndfi[,2],order.by=as.Date(anndfi[,1]))
anns <- window(annli,start="2016-01-01")

# 6.3.2. Artificial Neural Network Regression trading signals
annsig <- Lag(ifelse(Lag(anns)<0&anns>0,1,ifelse(Lag(anns)>0&anns<0,-1,0)))
annsig[is.na(annsig)] <- 0

# 6.3.3. Artificial Neural Network Regression trading positions
annpos <- ifelse(annsig>1,1,0)
for(i in 1:length(annpos)){annpos[i] <- ifelse(annsig[i]==1,1,ifelse(annsig[i]==-1,0,annpos[i-1]))}
annpos[is.na(annpos)] <- 0
anntr <- cbind(anns,annsig,annpos)
colnames(anntr) <- c("anns","annsig","annpos")
View(anntr)

# 7. Machine Trading Strategies Performance Comparison

# 7.1. Ensemble Method Trading Strategy Performance Comparison
xgbmret <- xgbmpos*rspys[,1]
xgbmretc <- ifelse((xgbmsig==1|xgbmsig==-1)&xgbmpos!=Lag(xgbmpos),(xgbmpos*rspys[,1])-0.001,xgbmpos*rspys[,1])
xgbmcomp <- cbind(xgbmret,xgbmretc,rspys[,1])
colnames(xgbmcomp) <- c("xgbmret","xgbmretc","rspy")
table.AnnualizedReturns(xgbmcomp)
charts.PerformanceSummary(xgbmcomp)

# 7.2. Maximum Margin Method Trading Strategy Performance Comparison
rsvmret <- rsvmpos*rspys[,1]
rsvmretc <- ifelse((rsvmsig==1|rsvmsig==-1)&rsvmpos!=Lag(rsvmpos),(rsvmpos*rspys[,1])-0.001,rsvmpos*rspys[,1])
rsvmcomp <- cbind(rsvmret,rsvmretc,rspys[,1])
colnames(rsvmcomp) <- c("rsvmret","rsvmretc","rspy")
table.AnnualizedReturns(rsvmcomp)
charts.PerformanceSummary(rsvmcomp)

# 7.3. Multi-Layer Perceptron Method Trading Strategy Performance Comparison
annret <- annpos*rspys[,1]
annretc <- ifelse((annsig==1|annsig==-1)&annpos!=Lag(annpos),(annpos*rspys[,1])-0.001,annpos*rspys[,1])
anncomp <- cbind(annret,annretc,rspys[,1])
colnames(anncomp) <- c("annret","annretc","rspy")
table.AnnualizedReturns(anncomp)
charts.PerformanceSummary(anncomp)

# 7.4. Machine Trading Strategies Performance Comparison

# 7.4.1. Without Trading Commissions
comp <- cbind(xgbmret,rsvmret,annret,rspys[,1])
colnames(comp) <- c("xgbmret","rsvmret","annret","rspy")
table.AnnualizedReturns(comp)
charts.PerformanceSummary(comp)

# 7.4.2. With Trading Commissions
compc <- cbind(xgbmretc,rsvmretc,annretc,rspys[,1])
colnames(compc) <- c("xgbmretc","rsvmretc","annretc","rspy")
table.AnnualizedReturns(compc)
charts.PerformanceSummary(compc)
