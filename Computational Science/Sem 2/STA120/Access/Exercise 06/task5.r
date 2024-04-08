mydata <- matrix(c(9, 5, 18, 22), nrow = 2, ncol = 2, byrow = TRUE,
                dimnames = list(c("Cleared", "Not cleared"),
                                c("Treatment A", "Treatment B")))

# null hypothesis: the proportions in both groups are the same.
prop_p_val <- prop.test(mydata)$p.value
prop_ci <- prop.test(mydata)$conf.int

fisher_p_val <- fisher.test(mydata)$p.value
fisher_ci <- fisher.test(mydata)$conf.int

sol <- list(prop_p_val = prop_p_val, prop_ci = prop_ci, fisher_p_val = fisher_p_val, fisher_ci = fisher_ci)

print(sol)
