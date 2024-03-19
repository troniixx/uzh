png(file="solution.png")

set.seed(100)
n <- 100

# What would be the best way to sample something once, but to have 500 samples?
# Generate a matrix with dimensions 500 rows by 'n' columns, 
# where each element is drawn from an exponential distribution with a rate parameter of 2.
artificial <- matrix(rexp(100*500, rate = 2) , 500, n)

# Find the minimum of each sample. You can use the function apply().
rowmins <- apply(artificial, 1, min)

par(mfrow = c(1, 2))
hist(rowmins, prob = TRUE, xlab = "Sample minima", ylim = c(0, n*2),
   main = "", breaks = 30) # default value for breaks is a bit too small
rug(rowmins) # in case `breaks` are not optimal 

# Compare it  with theoretical density using curve() function
curve(dexp(x, rate = 100*2) , col = "red", add = TRUE) # theoretical density like in the previous task

### Additionaly plot the  QQ-plot against theoretical quantile fucntion.
qqplot( qexp(ppoints(100), rate = 2*n) , rowmins, xlab = "Exp(2n)")
qqline( rowmins , distribution = function(p){qexp(p, rate = 2*n)} )

dev.off()
