#Given a number N, write a program to pint an Inverted Hollow Pyramid of 2*N-1 rows using numbers.
N = int(input())
for i in range(1,N):
    if(i==1):
        print("  "*(N-i)+str(i))
    else:
        print("  "*(N-i)+str(i)+" "+"  "*(i-2)+str(i))
for j in range(N,0,-1):
    if(j==1):
        print("  "*(N-j)+str(j))
    else:
        print("  "*(N-j)+str(j)+" "+"  "*(j-2)+str(j))
