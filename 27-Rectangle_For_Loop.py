#Write a program that reads two numbers M and N, and prints a Rectangle of M rows and N columns using numbers.
#Example of output:
#1 1 1 1
#2 2 2 2
#3 3 3 3
M = int(input())
N = int(input())
for i in range(1,M+1):
    print((str(i) + " ")*N)
