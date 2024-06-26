require(MASS)
data("anorexia")

cbt <- anorexia[anorexia$Treat == "CBT",]

tt <- t.test(cbt$Prewt, cbt$Postwt, paired = TRUE)
p_value = tt$p.value
ci <- tt$conf.int
alt_hyp <- tt$alternative

sol <- list(p_value = p_value, ci = ci, alt_hyp = alt_hyp)

print(sol)