# Problem 1
# Author: Mert Erol

# a)
protein <- read.csv("/Users/merterol/Desktop/iMac27_github/uzh/Computational Science/Sem 3/STA121/Sheet 2/protein.txt", sep = "\t")
rownames(protein) <- protein[, 1]
protein <- protein[, -1]

print(head(protein))
print(str(protein))

print(apply(protein, 2, sd))
print(apply(protein, 2, mean))

pca <- prcomp(protein, scale = TRUE, center = TRUE)
par(pty = "s")
screeplot((pca))

biplot(pca, col = c("red", "blue"))

print(pca$sdev^2)

print(cumsum(pca$sdev^2)/9)


#b)


