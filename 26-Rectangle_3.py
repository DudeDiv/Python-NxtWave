#Write a program that reads two numbers M and N, and prints a Rectangle of M rows and N columns using the numbers from 1.
M = int(input())
N = int(input())
counter = 1
while (counter<=M):
    print((str(counter) + " ")*N)
    c = int(counter)
    counter = counter + 1
