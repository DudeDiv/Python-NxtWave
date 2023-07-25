#Given a number N, write a program to print the sum of the Kth power of all the digits in the given number.
#K indicates the number of digits of the number N.
N = input()
K = len(N)
sum = 0
for i in N:
    sum = sum + int(i)**K
print(sum)
