#Write a program that reads two numbers M and N, and finds the product of the numbers from M to N that are divisible by 3.
#Print the product of the numbers from M to N that are divisible by 3. If there are no numbers that are divisible by 3 from M to N. Otherwise, print 1.
M = int(input())
N = int(input())
product = 1
for i in range(M,N+1):
    if(i%3==0):
        product = product * i
print(product)
