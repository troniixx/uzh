HbSb <- c(8.1, 9.2, 10, 10.4, 10.6, 10.9, 11.1, 11.9, 12.0, 12.1)

tt_two_sided <- t.test( HbSb , mu = 10 ) # same call as in Task 01
tt_one_sided <- t.test( HbSb , mu = 10 , alternative = "greater" )

p_ratio <- tt_two_sided$p.value / tt_one_sided$p.value
# What is the ratio of the two p values? Numerator the one like Task 01, Denominator the current one.

sol <- list(ratio = p_ratio)

print(sol)