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

