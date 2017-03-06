def fibonacci(max_dig=100):
    fib=[1,1]
    while len(str(fib[-1]))<max_dig:
        fib.append(fib[-1]+fib[-2])

    return fib

    
    
