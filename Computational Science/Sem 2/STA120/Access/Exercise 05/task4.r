require(MASS)
data(anorexia)

tt <- t.test(anorexia$Prewt, anorexia$Postwt, paired = TRUE)

p_value <- tt$p.value
ci <- tt$conf.int
alt_hyp <- tt$alternative

sol <- list(p_value = p_value, ci = ci, alt_hyp = alt_hyp)

print(sol)