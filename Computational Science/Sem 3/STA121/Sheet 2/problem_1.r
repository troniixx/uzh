# Problem 1
# Author: Mert Erol, Kasper Powell, Ishana Rana

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
# There are 9 components that can be identified, based on the loading vectors.
# Each component enscribes a source of protein, with clearly identifiable clusters.
# For example, many eastern european countries are clustered around cereals.
# Also, many middle- and western european countries are clustered around red and white meat,
# or eggs and milk. These clear groupings seem to highlight distinguishable preferences
# for certain sources of protein.
