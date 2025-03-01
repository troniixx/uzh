png(file="solution.png")
    set.seed(16)
    mydata <- read.table("resource/10salary.txt", header = TRUE, sep = ",")
    head(mydata)
    dim(mydata)
    str(mydata)
    # we need to convert 'District' into factor
    factor_district <- as.factor( mydata$District )
    pairs(factor_district ~ mydata$districtSize, gap = 0, main = "Pairs plot of the data")
dev.off()