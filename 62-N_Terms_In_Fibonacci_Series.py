#Write a program to recursively create a list of N Fibonacci terms.
#A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8...
#The first two terms are 0 and 1. All other terms are obtained by adding the preceding two terms.
def fibonacci(n):
    if(n<=1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def get_fibonacci_series(n):
    fibonacci_series = []
    for i in range(n):
        fibonacci_series.append(fibonacci(i))
    return fibonacci_series

n = int(input())
result = get_fibonacci_series(n)
print(result)
