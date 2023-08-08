#Given a number N, write a program to print the letter W of N rows using stars ( * ).
N = int(input())
print("* "*(2*N-1))
for i in range(1,N):
    print(" "*i + "* "*(N-i) + "  "*(i-1) + "* "*(N-i))
