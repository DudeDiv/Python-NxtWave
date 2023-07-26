#Write a program to check whether the given number is a perfect number or not.
#A number is considered as a Perfect number if sum of all factors excluding itself is equal to the number.
N = int(input())
sum = 0
for i in range(1,N):
    if(N%i==0):
        sum = sum + i
if(sum==N):
    print("Perfect Number")
else:
    print("Not a Perfect Number")
