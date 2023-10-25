data <- read.csv("/Users/merterol/uzh/Computational Linguistics/Computational Processing of Speech Rhythm/R not so Basic Practice/nlsy.csv", header = TRUE, sep = ",")
data <- na.omit(data)

# a) Datensätze definieren
set.seed(420)
size <- round(nrow(data)/3)
testing <- sample(1:nrow(data), size, replace = FALSE)

training <- data[-testing,]
testing <- data[testing,]

#b) lineare Regression

lin_reg <- lm(`lnearn` ~ `iq`, data = training)
summary(lin_reg)