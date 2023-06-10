#Write a program that reads a string and prints the first and last characters of the given string and prints the stars(*) instead of remaining characters.
a = input()
print(a[0]+("*"*(len(a)-2))+a[len(a)-1])
