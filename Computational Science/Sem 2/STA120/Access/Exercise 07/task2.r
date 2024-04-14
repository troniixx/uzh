mydata <- read.csv("resource/07water_transfer.txt")
str(mydata) # Structure of the dataset
table(mydata$age) # How many observations do we have per group?

#Wilcoxon-Mann-Whitney test
wilcox <- wilcox.test(pd ~ age , data = mydata)

sol <- list(wilcox$p.value)