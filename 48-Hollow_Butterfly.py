#Given a number N, write a program to print a Hollow Butterfly of 2*N rows using stars (*).
N = int(input())
K = N-2
for i in range(1,N+1):
    if(i==1):
        print("* "+"  "*(2*N-2)+"*")
    else:
        print("* "+"  "*(i-2)+"* "+"  "*K+"  "*K+"* "+"  "*(i-2)+"*")
        K = K-1
L = 0
for j in range(N,0,-1):
    if(j==1):
        print("* "+"  "*(2*N-2)+"*")
    else:
        print("* "+"  "*(j-2)+"* "+"  "*L+"* "+"  "*(j-2)+"*")
        L = L+2
