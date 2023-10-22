library(dplyr)
library(tidyr)
library(ggplot2)
library(nycflights13)
library(dlookr)
library(cowplot)
library(modelr)

data <- read.csv("/Users/merterol/uzh/Computational Linguistics/Computational Processing of Speech Rhythm/Assignment 1/Testing/table_Mert.csv")

#Variables incase we need them:
var1 <- "n"
var2 <- "rate"
var3 <- "mean"
var4 <- "meanLn"
var5 <- "delta"
var6 <- "deltaLn"
var7 <- "varco"
var8 <- "rPVI"
var9 <- "nPVI"
var10 <- "percentV"


#str(data)
#describe(data)
#summary(data)

#data %>% correlate() %>% plot()

# Create a box plot for all 10 variables
data_long <- gather(data, key = "Variable", value = "Value", var1:var10)
ggplot(data_long, aes(x = "", y = Value, fill = Variable)) +
    geom_boxplot() +
    labs(title = "Box Plot for Multiple Variables", y = "Value") +
    theme_minimal() +
    theme(legend.title = element_blank())

