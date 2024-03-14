png(file="solution.png")
  HbSS <- c(7.2, 7.7, 8, 8.1, 8.3, 8.4, 8.4, 8.5, 8.6, 8.7, 9.1, 
            9.1, 9.1, 9.8, 10.1, 10.3)
  HbSb <- c(8.1, 9.2, 10, 10.4, 10.6, 10.9, 11.1, 11.9, 12.0, 12.1)
  boxplot(list(HbSS = HbSS , HbSb = HbSb ), col = c(3, 4)) 
dev.off()