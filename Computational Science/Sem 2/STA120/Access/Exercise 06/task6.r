ORCI <- function(x1, x2, n1, n2, alpha = 0.05) {
    p1 <- x1 / (n1 - x1)
    p2 <- x2 / (n2 - x2)
    z <- qnorm(1 - alpha / 2)
    log_se <- sqrt(1/x1 + 1/(n1-x1) + 1/x2 + 1/(n2-x2))
    log_or <- log(p1) - log(p2)
    
    CI <- exp(log_or + c(-1, 1) * z * log_se)
    return(round(CI, 4))
}

RRCI <- function(x1, x2, n1, n2, alpha = 0.05) {
    p1 <- x1 / n1
    p2 <- x2 / n2
    z <- qnorm(1 - alpha/2)
    log_rr <- log(p1) - log(p2)
    log_se <- sqrt(1/x1 - 1/n1 + 1/x2 - 1/n2)
    
    CI <- exp(log_rr + c(-1, 1) * z * log_se)
    return(round(CI, 4))
}

OR_CI <- ORCI(x1 = 9, x2 = 5, n1 = 27, n2 = 27)
RR_CI <- RRCI(x1 = 9, x2 = 5, n1 = 27, n2 = 27)

sol <- list(OR_CI = OR_CI, RR_CI = RR_CI)
print(sol)
