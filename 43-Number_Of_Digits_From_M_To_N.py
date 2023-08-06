#Given two numbers M and N, write a program to print the count of the total numbers of digits from M to N.
M = int(input())
N = int(input())
digits = 0
for i in range(M,N+1):
    digits += len(str(i))
print(digits)
