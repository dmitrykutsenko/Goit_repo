'''
Create a caching_fibonacci() function that will have a cache of precomputed Fibonacci numbers. Inside it contains the function fibonacci(n), which will directly calculate the Fibonacci number itself. The caching_fibonacci() function returns the fibonacci function

If the Fibonacci number is stored in the cache dictionary, the fibonacci function returns the number from the cache. If it is not in the cache, then we calculate the number and put it in the cache, and return from the fibonacci function.
'''

def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n in cache:
            return cache[n]
        elif n <= 1:
            return n
        else:
            fib_num = fibonacci(n-1) + fibonacci(n-2)
            cache[n] = fib_num
            return fib_num

    return fibonacci