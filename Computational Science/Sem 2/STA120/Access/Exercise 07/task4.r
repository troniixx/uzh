png(file="solution.png")
    require(MASS)
    # Try to replace "%%%" with with proper operator, to get the right output.
    # This might help: https://www.statmethods.net/management/operators.html
    myAnorexia <- anorexia[ anorexia$Treat == "Cont" | anorexia$Treat == "FT", ] # Make sure you choose proper groups.
    myAnorexia <- droplevels(myAnorexia)

    # Calculate the difference between Postwt and Prewt: 
    anorexiaDiff <- myAnorexia$Postwt - myAnorexia$Prewt
    
    boxplot( anorexiaDiff ~ myAnorexia$Treat, 
            xlab = "Treatment", ylab = "Weight difference")
dev.off()
