#Given an integer N, and exponent M as input, write a program to calculate N power M without using the power operator(**).
N = int(input())
M = int(input())
product = 1
for i in range(M):
    product = product * N
print(product)
