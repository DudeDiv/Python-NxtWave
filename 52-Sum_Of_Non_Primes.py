#Write a program to print the sum of non-primes in the given N numbers. The numbers which are not primes are considered as non-primes.
N = int(input())
result = 0
factor = 0
for i in range(1,N+1):
    number = int(input())
    for j in range(1,number+1):
        if(number%j==0):
            factor += 1
    if(factor>2):
        result += number
    factor = 0
print(result)
