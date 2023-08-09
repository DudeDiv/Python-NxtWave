#Given a number N, write a program to print the Hollow Diamond of 2*N-1 rows using stars (*).
N = int(input())
for i in range(1,N):
    if(i==1):
        print(" "*(N-i)+"*")
    else:
        print(" "*(N-i)+"*"+" "*(2*i-3)+"*")
for j in range(N,0,-1):
    if(j==1):
        print(" "*(N-j)+"*")
    else:
        print(" "*(N-j)+"*"+" "*(2*j-3)+"*")
