mydata <- matrix(c(9, 5, 18, 22), nrow = 2, ncol = 2, byrow = TRUE,
                dimnames = list(c("Cleared", "Not cleared"),
                                c("Treatment A", "Treatment B")))

# null hypothesis: the proportions in both groups are the same.
alpha = 0.05
prop_p_val <- prop.test(mydata, conf.level = 1 - alpha)$p.value
prop_ci <- fisher.test(mydata, conf.level = 1 - alpha)$conf.int

sol <- list(prop_p_val = prop_p_val, prop_ci = prop_ci)

print(sol)