# Problem 1

# a)
set.seed <- 15
n <- 15
beta_0 <- 1
beta_1 <- 2
mu <- 4
sigma_x <- 4
sigma <- 2

x <- rnorm(n, mu, sigma_x)
y <- beta_0 + beta_1 * x + rnorm(n, 0, sigma)
plot(y ~ x)
(m1 <- lm(y ~ x))

abline(beta_0, beta_1)
abline(m1, lty = 2)
legend("topleft", legend = c("True", "Estimated"), lty = 1:2, bty = "n")


# b)
R <- 1000
coefs <- matrix(0, R, 2)

for (i in 1:R){
    y <- beta_0 + beta_1 * x + rnorm(n, 0, sigma)
    coefs[i, ] <- coef(lm(y ~ x))
}

str(coefs)

par(mfrow = c(1, 2))
hist(coefs[, 1], main = expression(beta[0]))
hist(coefs[, 2], main = expression(beta[1]))

# c)

R <- 1000
coefs <- matrix(0, R, 2)

for (i in 1:R){
    x <- rnorm(n, 4, sigma_x)
    y <- beta_0 + beta_1 * x + rnorm(n, 0, sigma)
    coefs[i, ] <- coef(lm(y ~ x))
}

par(mfrow = c(1, 2))
hist(coefs[, 1], main = expression(beta[0]))
hist(coefs[, 2], main = expression(beta[1]))

# Problem 2

# a)
set.seed(123)
require(fma)
bicoal

year <- c(time(bicoal))
coal <- as.numeric(bicoal)
df <- data.frame(coal = coal, year = year)
rss <- matrix(NA, ncol = 8, nrow = 100)
par(mfrow = c(2, 4))

for (deg in 1:8) {
    plot(year, coal, pch = 20, main = expression(paste("Degree ", deg)))
    
    for (i in 1:100) {
        train <- sort(sample(1:49, 38))

        fit <- lm(coal ~ poly(year, deg), data = df, subset = train)

        if (!is.null(fit)) {
            valid <- predict(fit, df[-train, ])
            
            if (length(valid) == length(df$coal[-train])) {
                rss[i, deg] <- sum((valid - df$coal[-train])^2)
            }

            lines(year[train], fit$fitted.values, col = "red")
        } else {
            warning(paste("Fit failed for degree", deg, "iteration", i))
        }
    }
}

par(mfrow = c(1, 1))

best_degree <- which.min(apply(rss, MARGIN = 2, median))
print(paste("Best degree:", best_degree))

boxplot(log(rss), main = expression(paste("log(rss) by degree")))
abline(h = c(mean(log(rss)), median(log(rss))), col = c("blue", "red"), lty = c(2,2))

# b
set.seed(123)
years <- 1920:1968
coal <- as.numeric(bicoal)
df <- data.frame(coal = coal, year = years)
test <- df[c(1:5, 45:49), ]
new_df <- df[6:44, ]
rss <- matrix(NA, ncol = 8, nrow = 100)

par(mfrow = c(2, 4))

for (deg in 1:8){
    plot(years, coal, pch = 20, main = expression(paste("Degree ", deg)))
    
    for (i in 1:100){
        train <- sort(sample(1:44, 38))
        
        fit <- lm(coal ~ poly(year, deg), data = df, subset = train)
        
        if (!is.null(fit)){
            valid <- predict(fit, df[-train, ])
            
            if (length(valid) == length(df$coal[-train])){
                rss[i, deg] <- sum((valid - df$coal[-train])^2)
            }
            
            lines(years[train], fit$fitted.values, col = "red")
        } else {
            warning(paste("Fit failed for degree", deg, "iteration", i))
        }
    }
}

# Set up plotting layout
par(mfrow = c(1, 2))

best_degree <- which.min(apply(rss, MARGIN = 2, median))
print(paste("Best degree based on minimum median RSS:", best_degree))

boxplot(log(rss), main = expression(paste("log(rss) by degree")))
abline(h = c(mean(log(rss)), median(log(rss))), col = c("blue", "red"), lty = c(2, 2))

fit <- lm(coal ~ poly(year, 5), data = df)
predictions <- predict(fit, test)
test_set <- sum((predictions - test$coal)^2)

boxplot(log(rss[, 7]), main = expression(paste("log(rss) for degree 7")))
abline(h = log(test_set), col = "red", lty = 2)
