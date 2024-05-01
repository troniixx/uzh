png(file="solution.png")
    set.seed(16)
    mydata <- read.table("resource/10salary.txt", header = TRUE, sep = ",")
    fit1 <- lm( ... ~ ... , data = mydata, subset = mydata$districtSize==...)
    summary(fit1)
    fit2 <- lm( ... ~ ... , data = mydata, subset = mydata$districtSize==...)
    summary(fit2)
    fit3 <- lm( ... ~ ... , data = mydata, subset = mydata$districtSize==...)
    summary(fit3)
    plot(... , ... , xlab = "Experience", ylab = "Salary", 
        col = ... , main = "Salary against experience")
    
    legend("bottomright", legend = c("districtSize 1", "districtSize 2", "districtSize 3"), pch = 1, 
        col = c("black", "red", "green"), bty = "n")
    abline(fit1, col = "black")
dev.off()