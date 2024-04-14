require(MASS)
myAnorexia <- anorexia[ anorexia$Treat == "Cont" | anorexia$Treat == "FT",] # Same split as in previous exercise.
myAnorexia <- droplevels(myAnorexia)

aCont <- myAnorexia[ anorexia$Treat == "Cont" ,] # Choose only Treat = "Cont"
wilcox_cont <- wilcox.test(aCont$Prewt, aCont$Postwt, paired = TRUE, exact = FALSE) #Prewt VS Postwt

aFT <- myAnorexia[myAnorexia$Treat == "FT",] # Choose only Treat = "FT"
wilcox_FT <- wilcox.test(aFT$Prewt, aFT$Postwt, paired = TRUE, exact = FALSE) #Prewt VS Postwt

sol <- list(wilcox_cont = wilcox_cont$p.value, wilcox_FT = wilcox_FT$p.value)
print(sol)