fizzbuzz <- function(upper){
    results <- character(upper)

    if(upper < 1){
        stop("Upper bound must be greater than 0")
    }

    for(each in 0:upper){
        if(each %% 3 == 0 && each %% 5 == 0){
            results[each] <- "fizzbuzz"
        }
        else if(each %% 3 == 0){
            results[each] <- "fizz"
        }
        else if(each %% 5 == 0){
            results[each] <- "buzz"
        }
        else{
            results[each] <- as.character(each)
        }
    }

    return(results)
}

result <- fizzbuzz(10)
cat(result, sep = "\n")