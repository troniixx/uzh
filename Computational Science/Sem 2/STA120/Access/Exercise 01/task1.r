png(file = "solution.png")
require(fields) # Or library(fields)

image.plot(volcano)
# function which.max() returns you the heighest value of your dataset (there is also which.min())

max_height <- which.max(volcano)
image.plot(volcano)
dev.off()

print(max_height)