

# Intermediate forecasting step as newdata needs to be same length as training range 
xgbmi <- predict.train(xgbmta,
                       newdata = rspyi) # inter

# Limited to trading range
xgbmdfi <- cbind(index(rspyi),
                 as.data.frame(xgbmi))
xgbmli <- xts(xgbmdfi[,2],order.by=as.Date(xgbmdfi[,1]))
xgbms <- window(xgbmli,start="2016-01-01")

# 6.1.2. eXtreme Gradient Boosting Regression trading signals
xgbmsig <- 
  Lag(ifelse(Lag(xgbms) < 0 & xgbms > 0, 1, 
             ifelse(Lag(xgbms) > 0 & xgbms < 0, -1, 0)))
xgbmsig[is.na(xgbmsig)] <- 0

# 6.1.3. eXtreme Gradient Boosting Regression trading positions
xgbmpos <- ifelse(xgbmsig>1,1,0)
for(i in 1:length(xgbmpos)) {
  xgbmpos[i] <- ifelse(xgbmsig[i] == 1,1,ifelse(xgbmsig[i]==-1,0,xgbmpos[i-1]))
}
xgbmpos[is.na(xgbmpos)] <- 0

xgbmtr <- cbind(xgbms, xgbmsig, xgbmpos)
colnames(xgbmtr) <- c("xgbms","xgbmsig","xgbmpos")
View(xgbmtr)

#                 xgbms       xgbmsig   xgbmpos
# 2016-01-04  0.0010576274       0       0
# 2016-01-05  0.0014915939       0       0
# 2016-01-06  0.0001849608       0       0
# 2016-01-07  0.0010576274       0       0
# 2016-01-08  0.0014915939       0       0
# 2016-01-11  0.0010576274       0       0
# 2016-01-12  0.0001849608       0       0
# 2016-01-13  0.0001849608       0       0
# 2016-01-14 -0.0004799857       0       0
# 2016-01-15 -0.0005528397      -1       0
# 2016-01-19  0.0014915939       0       0
# 2016-01-20  0.0001849608       1       1
# 2016-01-21  0.0010576274       0       1
# 2016-01-22  0.0001849608       0       1
# 2016-01-25 -0.0005528397       0       1
# 2016-01-26  0.0014915939      -1       0


# 6. Machine Trading Strategies

# 6.1. Ensemble Method Trading Strategy

# 6.1.1. eXtreme Gradient Boosting Regression forecasting


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
