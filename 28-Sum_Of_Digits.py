#Write a program to print the sum of all the digits in the given number.
num = input()
sum = 0
for i in range(0,len(num)):
    sum = sum + int(num[i])
print(sum)
