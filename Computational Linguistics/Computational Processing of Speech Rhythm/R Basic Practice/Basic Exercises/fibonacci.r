fibonacci <- function(num) {
    if (num <= 0) {
        return(0)
    } else if (num == 1) {
        return(1)
    }

    fib <- numeric(num)
    fib[1] <- 1
    fib[2] <- 1

    for (i in 3:num) {
        fib[i] <- fib[i - 1] + fib[i - 2]
    }

    return(fib[num])
}

result <- fibonacci(10)
print(result)
