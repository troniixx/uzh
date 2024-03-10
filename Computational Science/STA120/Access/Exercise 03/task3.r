png(file="solution.png")
set.seed(12)
n <- 100

# Sample the data
hist( rexp(n, rate = 2) , probability = TRUE, main = "") # Histogram of the sampled data with a superimposed theoretical density. 

# Using curve() function plot the theroretical function. For more info: ?curve()
curve(dexp(x, rate = 2), add = TRUE)

dev.off()
