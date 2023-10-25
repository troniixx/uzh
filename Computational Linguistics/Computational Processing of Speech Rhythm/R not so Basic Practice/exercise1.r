# Daten aus der CSV-Datei laden
data <- read.csv("/Users/merterol/uzh/Computational Linguistics/Computational Processing of Speech Rhythm/R not so Basic Practice/luft.csv", header = TRUE, sep = ",")
data <- na.omit(data)

# a) Lineare Regression
lin_reg <- lm(`ozon` ~ `Lufttemperatur`, data = data)

# Streudiagramm und Regressionsgerade zeichnen
plot(data$`Lufttemperatur`, data$`ozon`, main = "Scatter Plot", xlab = "Lufttemperatur", ylab = "Ozon (max)")
abline(lin_reg, col = "red")

# c) Konfidenzintervall
x_bar <- mean(data$`Lufttemperatur`)
conf_int <- predict(lin_reg, newdata = data.frame(`Lufttemperatur` = x_bar), interval = "confidence")

# d) Vorhersageintervall
pred_int <- predict(lin_reg, newdata = data.frame(`Lufttemperatur` = x_bar), interval = "prediction")


# f) 90% Vorhersageintervall für xneu = 150
x_new <- 150
pred_int_90 <- predict(lin_reg, newdata = data.frame(`Lufttemperatur` = x_new), interval = "prediction", level = 0.90)


cat("x_bar = ", x_bar, "\n")
cat("conf_int = ", conf_int, "\n")
cat("pred_int = ", pred_int, "\n")
cat("pred_int_90 = ", pred_int_90, "\n")
