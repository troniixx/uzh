ORCI <- function(x1, x2, n1, n2, alpha = 0.05) {
    
    ...
    
    CI <- exp( ... + c(-1, 1) * ... * ...)
    return(round(CI, 4))
}

RRCI <- function(x1, x2, n1, n2, alpha = 0.05) {

    ... 
    
    CI <- exp( ... + c(-1, 1) * ... * ...)
    return(round(CI , 4))
}

OR_CI <- ORCI(x1 = ... , x2 = ... , n1 = ... , n2 = ... )
RR_CI <- RRCI(x1 = ... , x2 = ... , n1 = ... , n2 = ... )

sol <- list(OR_CI = OR_CI, RR_CI = RR_CI)