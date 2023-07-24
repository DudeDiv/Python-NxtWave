#Write a program that reads two numbers M and N and prints odd numbers from M to N separated by a space.
M = int(input())
N = int(input())
result = ""
for i in range(M,N+1):
    if(i%2==1):
        result = result + str(i) + " "
print(result)
