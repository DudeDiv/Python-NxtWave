#Write a program to print if the given number is divisible by any of the lucky numbers 6, 3, 2 in decreasing order of priority.
#Print "Number is divisible by" followed by the luckiest number among the above 3 which can divide the number.
#Print "Number is not divisible by 2, 3 or 6" if the number is not divisible by any of them.
N = int(input())

if(N%6==0):
    print("Number is divisible by 6")
if(N%3==0 and N%6!=0 and N%2!=0):
    print("Number is divisible by 3")
if(N%2==0 and N%3!=0 and N%6!=0):
    print("Number is divisible by 2")
if(N%2!=0 and N%3!=0 and N%6!=0):
    print("Number is not divisible by 2, 3 or 6")
