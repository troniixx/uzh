### This is an R tutorial using the iris dataset (Fisher, 1936). ###
### We will see the basics of R and R scripts: ###
###   how to load data, basic data types, basic commands, packages, and plots ###
### Alessandro De Luca, HS22 ###

rm(list = ls()) # clear R's brain

# data types #
x <- 1 # this is an integer (double)
typeof(x)
x <- 1.1 # this is also a number (double)
typeof(x)
x <- "hello world" # this is a string/character (character)
typeof(x)
x <- TRUE # this is a boolean value (logical)
typeof(x)
x <- FALSE # the only other logical value possible
x <- NA # this works just like FALSE but stands for "not a number"
typeof(x)

x <- c(1, 2, 3) # this is a vector of numbers (double/numeric): vectors are created using "c()"
typeof(x)
x <- c(TRUE, FALSE, TRUE) # you can create vectors containing any elements
typeof(x)
x <- c(1, TRUE) # but if elements are of different types a common type is used
typeof(x)
x <- c(1, "hello")
typeof(x)

# changing data type
x <- "1"
typeof(x)
x <- as.numeric(x)
typeof(x)


x <- 2:8 # creating a series of numbers
x
x <- seq(2, 8) # creating a series of numbers
x
typeof(x) # integer vector
x <- c(x, 42) # "appending" (adding) an element to a vector
x
x + 1 # simple addition
x + seq(2, 9) # vector addition (must have same length)
length(x) # vector dimensions

# dataframe
x <- data.frame("x" = x, "y" = x^2)
x
typeof(x)
class(x)

# mathematical operators
cat("classical math operators:
  +
  -
  *
  /")
cat("exponentiation: ^ or **")
cat("modulus: %% (the remainder of a division)")
5 %% 2 # example
cat("integer division: %/% (get only integer value of division")
5 %/% 2 # example

# logical operators
cat("comparisons:
      < less than; <= less or equal than
      > greater than; >= greater or equal than
      == equal to; != not equal to
      !x not x (if x = TRUE than !x = FALSE
      & and; | or")

# load in data #
iris <- read.csv("rTutorial/iris.csv")
head(iris) # only first 5 rows
tail(iris) # only last 5 rows
iris$Sepal.Length # only one column
iris[1] # same but...
typeof(iris$Sepal.Length) # vector
class(iris[1]) # data.frame

iris[1, 3] # column 1, row 3
iris$Sepal.Length[3] # same

# how many rows and columns?
dim(iris) # gives both rows and columns
nrow(iris)
ncol(iris)
colnames(iris) # column names

# summarising data #
str(iris)
summary(iris)

# libraries/packages
install.packages("ggplot2") # installing a library
install.packages("GGally")
library(ggplot2) # loading a library
library(GGally)
ggpairs(iris) # plot summary

# dplyr #
# very useful package to manipulate data
install.packages("dplyr")
library(dplyr)
glimpse(iris) # better summary than str in my opinion

unique(iris$Species) # unique values of the column 'Species'
setosa <- filter(iris, Species == "setosa") # filter with dplyr
glimpse(setosa)

virginica.length6 <- filter(iris, Species == "virginica", Sepal.Length > 6) # multiple filters
glimpse(virginica.length6)

iris.subset <- select(iris, Species, Sepal.Length, Sepal.Width) # select certain columns
glimpse(iris.subset)

iris.newcol <- mutate(iris, longer.sepal = Sepal.Length > Petal.Length) # add a new column
glimpse(iris.newcol)

# plotting #
plot(iris$Sepal.Width, iris$Sepal.Length) # easy scatter plot
hist(iris$Sepal.Length) # histogram

# ggplot for more control
ggplot(data = iris, mapping = aes(x = Sepal.Width, y = Sepal.Length, colour = Species)) +
  geom_point() + # scatter plot
  geom_smooth(method = "lm") # smooth line: in this case using a linear model
