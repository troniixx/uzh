n <- 95
x <- 8
p_ML <- x/n
omega_ML <- p_ML/(1-p_ML)

sol <- list(p_ML = p_ML, omega_ML = omega_ML)

print(sol)