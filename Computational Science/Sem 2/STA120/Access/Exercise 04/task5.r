require(spam) 
data(Oral) 

n <- 544
set.seed(3) 

bootstrap <- function(n.repl){
    smr <- numeric(n.repl)
    for(i in 1:n.repl){
        smr[i] <- mean(sample(Oral$SMR, n, replace = TRUE))
    }
    smr
}
# Room for creativity!

sol <- quantile(bootstrap(10000), c(0.025, 0.975)) 
