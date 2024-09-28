# Problem 2
# Author: Mert Erol

require(maps)
require(fields)
load("/Users/merterol/Desktop/iMac27_github/uzh/Computational Science/Sem 3/STA121/Sheet 2/prec_jan_feb.RData")

# a)
par(pty = "s", mfrow = c(2, 2), mar = c(2, 2, 2, 2))

image.plot(lon, lat, pre[, , 1], main = "January 1st, 00:00")
map("world", add = TRUE)

image.plot(lon, lat, pre[, , 2], main = "January 1st, 06:00")
map("world", add = TRUE)

image.plot(lon, lat, pre[, , 3], main = "January 1st, 12:00")
map("world", add = TRUE)

image.plot(lon, lat, pre[, , 4], main = "January 1st, 12:00")
map("world", add = TRUE)


# mean and variance field

par(pty = "s", mfrow = c(1, 2), mar = c(2, 2, 2, 2))

image.plot(lon, lat, apply(pre, c(1, 2), mean), main = "Mean")
map("world", add = TRUE)

image.plot(lon, lat, apply(pre, c(1, 2), var), main = "Variance")
map("world", add = TRUE)

# b)

dims_pre <- dim(pre)
pre_scaled <- t(array(pre, c(dims_pre[1] * dims_pre[2], dims_pre[3])))
pca <- prcomp(pre_scaled, scale = FALSE, center = TRUE)

print(names(pca))
print(str(pca))

par(pty = "s", mfrow = c(2, 2), mar = c(2, 2, 2, 2))

image.plot(lon, lat, array(pca$rotation[, 1], dim = dims_pre[1:2]))
map("world", add = TRUE)

image.plot(lon, lat, array(pca$rotation[, 2], dim = dims_pre[1:2]))
map("world", add = TRUE)

image.plot(lon, lat, array(pca$rotation[, 3], dim = dims_pre[1:2]))
map("world", add = TRUE)

image.plot(lon, lat, array(pca$rotation[, 4], dim = dims_pre[1:2]))
map("world", add = TRUE)

# c)

par(mfrow = c(1, 1))
var <- pca$sdev^2

plot(var[-length(var)], type = "o", log = "y")
plot(var[1:20], type = "o", log = "y", ylab = "Eigen")

# d)

v <- var
error <- sqrt(2/dim(pca$rotation)[2])
cut <- (v[-length(v)] - v[-1]) / v[-length(v)] < error

plot(var[1:20], type = "o", log = "y", ylab = "Eigen")
abline(v = which(cut) + 0.5, lty = 2, col = 2)