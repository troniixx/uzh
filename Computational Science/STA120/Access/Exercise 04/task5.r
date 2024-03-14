require(spam) 
data(Oral) 

n <- 544
set.seed(3) 

bootstrap <- function(n.repl){

}
# Room for creativity!

sol <- quantile(bootstrap(10000), c(0.025, 0.975)) 
