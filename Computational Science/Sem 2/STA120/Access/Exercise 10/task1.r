mydata <- read.table("resource/stackloss.txt", header = TRUE, sep = ",")
str(mydata)

par(mfrow = c(1, 4))
boxplot(mydata$Airflow, xlab = "Airflow")
boxplot(mydata$Temp, xlab = "Temp")
boxplot(mydata$Acid, xlab = "Acid.")
boxplot(mydata$Stackloss, xlab = "Stackloss")

# Be aware that you don't see how many outliers there are if they have the exact same value. 
# Boxplots give you an idea about the value range of outliers. 
# You can make them visible with pairs plots (for instance outliers from the variable Air in red).
pairs( ... , gap = 0, col = c(...>70)+1)

fit_full <- ...
summary( ... )
par(mfrow = c(2, 2))
plot( ... )

### Multicollinearity
print( ... ( mydata[c("Air", "Temp", "Acid.")] ))

# Looking at correlations alone is NOT sufficient to detecting multicollinearity
library(car)
vif( ... )

#Looking at step() we see that which predictor we can remove from our model.
step( ... )

#To investigate the effect of leaving out one observations, we use so-called leave-out-one diagnostics, 
#i.e. what would happen to our estimates if we deleted exactly one row from our dataset?
influence.measures( ... )

#Let us consider a smaller (nested) model, without the non-significant predictor:
fit_nested <- ...
summary(fit_nested)

#Below, fill out whether multicollinearity exists (Yes or No), which predictor can be removed (capital first letter), and the optimal model formula (lm(...))
sol <- list(Multicollinearity_exists = " ... ", predictor_that_can_be_removed = " ... ", optimal_model = ... )