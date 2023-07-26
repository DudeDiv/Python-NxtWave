#Given a number N, write a program to print the factors of the number N.
N = int(input())
for i in range(1,N+1):
    if(N%i==0):
        print(i)
