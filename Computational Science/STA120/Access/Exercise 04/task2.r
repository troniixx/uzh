png(file="solution.png")
  HbSS <- c(7.2, 7.7, 8, 8.1, 8.3, 8.4, 8.4, 8.5, 8.6, 8.7, 9.1, 
            9.1, 9.1, 9.8, 10.1, 10.3)
  HbSb <- c(8.1, 9.2, 10, 10.4, 10.6, 10.9, 11.1, 11.9, 12.0, 12.1)
  qqnorm( HbSS , xlim = c(-2, 2), ylim = c(7, 12), col = 3, main = "")
  qqline(HbSS, col = 3)

  # Now make the HbSb QQ-plot but do not plot it. 
  #boxplot(list(HbSS = HbSS , HbSb = HbSb ), col = c(3, 4))
  # Instead take out the points of the QQ-plot and add them to the original plot.
  # At the end you have to have one plot only.
  tmp <- qqnorm(HbSb, plot.it = FALSE) # is there a away not to plot it and just save it? You can have a look at the qqnorm function's documentation if you are not sure.
  points(tmp, col = 4)
  qqline(HbSb, col = 4)
dev.off()