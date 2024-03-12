#Write a program to recursively find the Nth term in the Fibonacci series.
def fibonacci(n):
    if(n<=1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input())
result = fibonacci(n)
print(result)
