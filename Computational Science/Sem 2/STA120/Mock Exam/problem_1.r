library(ggplot2)

# **** Task a) ****
#load dataset
data <- read.csv("/Users/merterol/uzh/Computational Science/Sem 2/STA120/Mock Exam/birds.csv")

#exploratory data analysis
str(data)
summary(data)

# Boxplot to compare decibels between urban and rural settings
boxplot(decibels ~ Urban, data = data, main = "Bird Song Volume by Location", xlab = "Urban Noise", ylab = "Decibels")

# Histograms by group
hist(data$decibels[data$Urban == TRUE], main = "Decibels in Urban Areas", xlab = "Decibels", col = "blue")
hist(data$decibels[data$Urban == FALSE], main = "Decibels in Rural Areas", xlab = "Decibels", col = "green")


# **** Task b) ****

#t-test
t.test(data$decibels ~ data$Urban)

# **** Task c) ****

#permutation test function
perm_test <- function(data, num_permutations = 1000){
    r <- 1000
    tobs <- median(data$decibels[data$Urban == TRUE]) - median(data$decibels[data$Urban == FALSE])
    all_data <- c(data$decibels[data$Urban == TRUE], data$decibels[data$Urban == FALSE])
    tsim <- array(0, r)

    for(i in 1:r){
        index <- sample(1:length(all_data), length(data$decibels[data$Urban == TRUE]), replace = F) #nolint
        medianxA <- median(all_data[index])
        medianxB <- median(all_data[-index])
        tsim[i] <- medianxA - medianxB
    }

    return(sum(abs(tsim) >= abs(tobs))/ r)
}
#run permutation test
perm_test(data, 41)