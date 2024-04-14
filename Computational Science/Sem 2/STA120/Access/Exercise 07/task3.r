mydata <- read.csv("resource/07water_transfer.txt")

perm_test <- function(x, y){
    R <- 1000
    # Store the "original" observed median difference
    tobs <- median(x) - median(y)
    # Store the data without the group labels ( try using c() )
    all.data <- c(x, y)
    tsim <- array(0, R) # Preallocation of R-amount of values

    for(i in 1:R ){
        index <- sample(1:length(all.data), length(x), replace = F) # random permutation # nolint
        medianxA <- median(all.data[index]) # Sample median of group A
        medianxB <- median(all.data[-index]) # Sample median of group B
        tsim[i] <- medianxA - medianxB  # Difference for the current iteration
    }

    # Sample p-value. Proportion of "some" values and amount of iterations  
    return( sum(abs(tsim) >= abs(tobs))/ R)  
}

# We test our function:
yA <- mydata[mydata$age == "12-26 Weeks", 1]  # Split the data such that you have one factor per group
yB <- mydata[mydata$age == "At term", 1] # Split the data such that you have one factor per group

set.seed(14)
permtest <- perm_test(yA, yB)

sol <- list(permtest = permtest)
print(sol)