png(file="solution.png")
dat <- read.csv("resource/wolvesmoose.csv", header=TRUE)
par(mfrow = c(2,3))

boxplot(dat$Moose, dat$Wolf)

qqnorm(dat$Moose, main="QQ-plot Moose")
qqline(dat$Moose)

qqnorm(dat$Wolf, main="QQ-plot of Wolves")
qqline(dat$Wolf)

plot(Wolf ~ Year, data = dat, type = "l")
plot(Moose ~ Year, data = dat,  type = "l")

# How many times should the colors repeat so that the legend makes sense?
plot(Wolf ~ Moose, data = dat, col=rep( c(1,2,3), times=c(1, 1, 1)))


legend("topright", col=c(1,2,3), 
    legend=c("1959-1980","1981-1996","1997-2011"), 
    bty="n", 
    pch="o")

dev.off()
