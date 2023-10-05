#Given a integer N, write a program to print the sandglass star pattern, similar to the pattern shown below.
N = int(input())
for i in range(0,N-1):
    print(" "*i + "* "*(N-i))
for j in range(1,N+1):
    print(" "*(N-j)+"* "*j)
