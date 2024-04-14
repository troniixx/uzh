require(MASS)
myAnorexia <- anorexia[ anorexia$Treat == "Cont" | anorexia$Treat == "FT", ] # Same split as in previous exercise.
myAnorexia <- droplevels(myAnorexia)
anorexiaDiff <- myAnorexia$Postwt - myAnorexia$Prewt # Difference as in previous exercise.

wilcox <- wilcox.test(anorexiaDiff ~ myAnorexia$Treat , exact = FALSE)

sol <- list(wilcox = wilcox$p.value)
print(sol)