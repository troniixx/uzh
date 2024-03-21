HbSS <- c(7.2, 7.7, 8, 8.1, 8.3, 8.4, 8.4, 8.5, 8.6, 8.7, 9.1,
        9.1, 9.1, 9.8, 10.1, 10.3)
HbSb <- c(8.1, 9.2, 10, 10.4, 10.6, 10.9, 11.1, 11.9, 12.0, 12.1)

tt <- t.test(HbSS, HbSb, var.equal = FALSE, conf.level = 0.99)

p_value = tt$p.value
ci <- tt$conf.int
alt_hyp <- tt$alternative

sol <- list(p_value = p_value, alt_hyp = alt_hyp)

print(sol)