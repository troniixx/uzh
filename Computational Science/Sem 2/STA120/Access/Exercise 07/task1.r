require(datasets)
data(mtcars)

# miles/gallon
location_mpg <-  c( mean(mtcars$mpg) ,            # Mean
                    mean(mtcars$mpg, trim = 0.1) , #10% Trimmed Mean
                    median(mtcars$mpg) )           # Median

spread_mpg <- c( sd(mtcars$mpg) ,                 # Standart deviation 
                IQR(mtcars$mpg) /1.349,           # IQR 
                mad(mtcars$mpg) )                 # MAD

# number of cylinders
location_cyl <- c(mean(mtcars$cyl) ,              # Mean
                    mean(mtcars$cyl, trim = 0.1) ,  #10% Trimmed Mean
                    median(mtcars$cyl) )            # Median

spread_cyl <- c(sd(mtcars$cyl) ,                  # Standart deviation 
                IQR(mtcars$cyl) /1.349,           # IQR 
                mad(mtcars$cyl) )                 # MAD

# weight
location_wt <- c(
                mean(mtcars$wt),                        # Mean
                mean(mtcars$wt, trim = 0.1),            # 10% Trimmed Mean
                median(mtcars$wt)                       # Median
)
spread_wt <- c(
                sd(mtcars$wt),                          # Standard deviation
                IQR(mtcars$wt) / 1.349,                 # IQR scaled to SD
                mad(mtcars$wt)                          # MAD
)   

sol <- list(location_mpg = location_mpg, 
    spread_mpg = spread_mpg, 
    location_cyl = location_cyl, 
    spread_cyl = spread_cyl, 
    location_wt = location_wt, 
    spread_wt = spread_wt)