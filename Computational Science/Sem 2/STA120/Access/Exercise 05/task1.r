HbSb <- c(8.1, 9.2, 10, 10.4, 10.6, 10.9, 11.1, 11.9, 12.0, 12.1)
tt <- t.test( HbSb , mu = 10 )
sol <- list(ttest = tt)
print(sol)