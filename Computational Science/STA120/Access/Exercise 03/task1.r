png(file="solution.png")
    set.seed(3)
    lambda1 <- 0.2
    lambda2 <- 2
    n <- 200
    
    data1 <- ...
    data2 <- ...
    
    # Pay attention to the binning to be used for count data!
    par(mfrow = c(1, 2))
    hist( ... , xlab = "", prob = TRUE,
        breaks = seq(min(data1)-0.5, max(data1)+0.5, by = 1),
        main = expression(lambda == 0.2))
    points( ... , ... (unique( ... ), ... ), pch = 19)
    hist(data2, xlab = "", prob = TRUE,
        breaks = seq(min(data2)-0.5, max(data2)+0.5, by = 1),
        main = expression(lambda == 2))
    points( ... , ... (unique( ... ), lambda2), pch = 19)
dev.off()