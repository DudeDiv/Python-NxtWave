#Write a program to print the smallest number among given N numbers.
N = int(input())
first_input = int(input())
num = first_input
for i in range(N-1):
    num1 = int(input())
    if(num1<num):
        num = num1
print(num1)
