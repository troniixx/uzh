######################################################################################
# A brief tutorial on Exploratory Data Analysis                                      #
# Written by Alessandro De Luca on 12.10.2023                                        #
# for 23HS - Computational Processing of Speech Rhythm for Language and              #
#            Speaker Classification.                                                 #
# Copyright: CC0 No rights reserved.                                                 #
#                                                                                    #
# Inspiration: https://r4ds.had.co.nz/exploratory-data-analysis.html#prerequisites-3 #
######################################################################################

# clear R's brain
rm(list = ls())

# Useful EDA libraries #
# remember that to install packages you have to run in the console
# install.packages("package name") or install.packages(c("package name 1", "package name 2"))
# or use the GUI installer provided within RStudio
library(dplyr) # for data wrangling
library(ggplot2) # for data visualization
library(nycflights13) # we'll use one of the datasets
library(dlookr) # a lot of EDA functions
library(cowplot) # for grid plotting
library(modelr) # to add residuals of lm

# Loading the data!
dd_diamonds <- diamonds # from the ggplot2 package
dd_flights <- nycflights13::flights

# general description of the data: need some transformations? #
str(dd_diamonds) # first we look at our data in general
describe(dd_diamonds) # we can use this to describe the data; similar to summary() in baseR
# hmmm... price and carat are positively skewed and price has a very large sd

# and what about the categorical variables?
summary(dd_diamonds)

# let's look at general relationships between the variables
dd_diamonds %>%
    correlate() %>%
    plot()
# we can see some expected relationships

# Let's go back to our problem of skeweness for price and carat
# we can look at the distribution of the variables using histograms
carat_hist <- ggplot(data = dd_diamonds) +
    geom_histogram(mapping = aes(x = carat), binwidth = 0.5)
price_hist <- ggplot(data = dd_diamonds) +
    geom_histogram(mapping = aes(x = price), binwidth = 500)
plot_grid(carat_hist, price_hist, nrow = 1, ncol = 2)
# Okay, they are skewed and we should transform them; but how?
plot_normality(dd_diamonds, carat, price) # this function can help

# To transform our data we can use dplyr
dd_diamonds <- dd_diamonds %>%
    mutate(log_carat = log(carat), log_price = log(price))
# But remember that if you use these in your model you have to backtransform the results
# e.g. what does a negative carat value mean?

# You can also look at histograms from the perspective of categorical variables
ggplot(data = dd_diamonds, mapping = aes(x = price, color = cut)) +
    geom_freqpoly(binwidth = 500)
# but it's more useful later on

# Outliers #
# First of all, what are not outliers?
ggplot(data = dd_diamonds, mapping = aes(x = carat)) +
    geom_histogram(binwidth = 0.01)
# maybe some subgroups? Is carat a truly continuous variable?

# sometimes outliers are difficult to see
ally <- ggplot(data = dd_diamonds) +
    geom_histogram(mapping = aes(x = y), binwidth = 0.5)
zoomy <- ggplot(data = dd_diamonds) +
    geom_histogram(mapping = aes(x = y), binwidth = 0.5) +
    coord_cartesian(ylim = c(0, 40))
plot_grid(ally, zoomy, nrow = 1, ncol = 2)
# There are some 'weird' values of y

unusual <- dd_diamonds %>%
    filter(y < 3 | y > 20) %>%
    select(price, x, y, z) %>%
    arrange(y)
unusual
# Should we drop them? Yes, No? WHY?

dd_diamonds2 <- dd_diamonds %>%
    mutate(y = ifelse(y < 3 | y > 20, NA, y)) # if y is less than 3 OR (|) y is more than 20: set the value to NA; otherwise leave it as is
# This way, when we run any model or plot the data we will be reminded of these strange values

ggplot(data = dd_diamonds2, mapping = aes(x = x, y = y)) +
    geom_point()
# Warning message:
# Removed 9 rows containing missing values (`geom_point()`).
# you can suppress the warning message by using na.rm = TRUE

# Missing values #
summary(dd_flights)
summary(dd_flights$dep_time)
dd_flights %>%
    filter(is.na(dep_time)) %>%
    count()
# Lots of NAs in dep_time -> WHY?

# missing dep_time = cancelled flight
dd_flights %>%
    mutate(
        cancelled = is.na(dep_time), # if NA than cancelled = TRUE
        sched_hour = sched_dep_time %/% 100,
        sched_min = sched_dep_time %% 100,
        sched_dep_time = sched_hour + sched_min / 60
    ) %>%
    ggplot(mapping = aes(sched_dep_time)) +
    geom_freqpoly(mapping = aes(color = cancelled), binwidth = 1 / 4)
# doesn't look so nice -> also no relationship (we'll see a better visualization later)

# Exploring relationships #
# two continuous variables
ggplot(data = dd_diamonds) +
    geom_point(mapping = aes(x = carat, y = price))
ggplot(data = dd_diamonds) +
    geom_point(mapping = aes(x = carat, y = price), alpha = 0.01) # when there are a lot of data points you can use transparency
ggplot(data = dd_diamonds) +
    geom_bin2d(mapping = aes(x = carat, y = price)) # or 2D bin the data
ggplot(data = dd_diamonds, mapping = aes(x = carat, y = price)) +
    geom_boxplot(mapping = aes(group = cut_width(carat, 0.1))) # or make a continuous variable categorical
ggplot(data = dd_diamonds, mapping = aes(x = carat, y = price)) +
    geom_boxplot(mapping = aes(group = cut_number(carat, 20))) # or make a continuous variable categorical

# a continous and a categorical variable
# going back to our frequency plot of cancelled and departed flights -> the problem is that we are looking at counts
# let's take a look at densities
dd_flights %>%
    mutate(
        cancelled = is.na(dep_time), # if NA than cancelled = TRUE
        sched_hour = sched_dep_time %/% 100,
        sched_min = sched_dep_time %% 100,
        sched_dep_time = sched_hour + sched_min / 60
    ) %>%
    ggplot(mapping = aes(x = sched_dep_time, y = after_stat(density))) +
    geom_freqpoly(mapping = aes(color = cancelled), binwidth = 1 / 4)
# we can see how the departure time and rate of cancellation or not are not related

# another example
ggplot(data = dd_diamonds, aes(x = price, y = after_stat(density))) +
    geom_freqpoly(mapping = aes(color = cut), binwidth = 500)

# or the BEST way: BOX PLOTS
ggplot(data = dd_diamonds, mapping = aes(x = cut, y = price)) +
    geom_boxplot()
# or violin plot
ggplot(data = dd_diamonds, mapping = aes(x = cut, y = price)) +
    geom_violin() +
    geom_boxplot(width = 0.1)
# are lower quality diamonds more expansive than higher quality diamonds???

# two categorical variables
# the relationship is shown in this way: how many observations appear in two categories of two different categorical variables
ggplot(data = dd_diamonds) +
    geom_count(mapping = aes(x = cut, y = color))
# or via tables
dd_diamonds %>%
    count(cut, color)

# Covariation and how it can impact relationships
# looking back at the correlations in the diamonds data and the interesting relationship between price and cut
cor(dd_diamonds[c("carat", "price")])
# carat and price are quite correlated
# Are there more larger diamonds that are 'Fair' cut?
ggplot(data = dd_diamonds, mapping = aes(x = carat)) +
    geom_freqpoly(mapping = aes(color = cut), binwidth = 0.1)
# Not really, but there are a lot of 'Ideal' diamonds that are very small
# You can see a relationship between carat and price also looking back at the scatter plot we had created (line 114)
# we can model the relationship between carat and price to remove the effect of carat to price when comparing cuts
mod <- lm(log_price ~ log_carat, data = dd_diamonds)
summary(mod)

dd_diamonds2 <- dd_diamonds %>%
    add_residuals(mod) %>%
    mutate(resid = exp(resid))
ggplot(data = dd_diamonds2, mapping = aes(x = carat, y = resid)) +
    geom_point(alpha = 0.1)
# no more relationship

# Now let's go back to the 'surprising' relationship we discovered before
ggplot(data = dd_diamonds2, mapping = aes(x = cut, y = resid)) +
    geom_boxplot()
# Looks much more reasonable
