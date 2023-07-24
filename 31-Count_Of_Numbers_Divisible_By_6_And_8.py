#Write a program that reads a number N and prints the count of numbers from 1 to N that are divisible by both 6 and 8.
N = int(input())
count = 0
for i in range(1,N+1):
    if(i%6==0 and i%8==0):
        count = count + 1
print(count)
