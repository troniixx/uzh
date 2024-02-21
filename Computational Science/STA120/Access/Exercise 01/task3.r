png(file="solution.png")
dat <- read.csv("Computational Science/STA120/Access/Exercise 01/wolvesmoose.csv", header=TRUE)

par(mfrow = c(2,3))

boxplot(dat$Wolf, dat$Moose, 
        names = c("Wolf Abundance", "Moose Abundance"), 
        main="Boxplot of Moose and Wolves")

qqnorm(dat$Moose, main="QQ-plot Moose")
qqline(dat$Moose)

qqnorm(dat$Wolf, main="QQ-plot of Wolves")
qqline(dat$Wolf)

plot(dat$Year, dat$Wolf, type = "l", main="Wolf Abundance over Year", xlab = "Year", ylab = "Wolf Abundance")
plot(dat$Year, dat$Moose,  type = "l", main="Moose Abundance over Year", xlab = "Year", ylab = "Moose Abundance")

# How many times should the colors repeat so that the legend makes sense?
plot(dat$Moose, dat$Wolf, col=rep( c(1,2,3), times=c(20, 25, 30)))


legend("topright", col=c(1,3,4), 
    legend=c("1959-1980","1981-1996","1997-2011"), 
    bty="n", 
    pch="o")

null <- dev.off()
