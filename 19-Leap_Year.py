#Write a program that reads a year Y and checks if the year Y is a leap year. A year is a leap year if any of the given conditions are satisfied:
#Y is divisible by 400.
#Y is divisible by 4, and not divisible by 100.
#Print True if any of the given conditions are satisfied. Otherwise, print False.
Y = int(input())
condition1 = Y%400==0
condition2 = Y%4==0 and Y%100!=0
if(condition1 or condition2):
    print(True)
else:
    print(False)
