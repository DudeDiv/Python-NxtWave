#Given two numbers M and N, write a program to find the count of numbers from M to N that are divisible by 6.
#Print "No Numbers Found" if the count of numbers from M to N that are divisible by 6 is 0.
#Otherwise, print the numbers from M to N that are divisible by 6 separated by a space.
M = int(input())
N = int(input())
count = 0
result = ""
for i in range(M,N+1):
    if(i%6==0):
        result = result + str(i) + " "
        count = count + 1
if(count == 0):
    print("No Numbers Found")
else:
    print(result)
