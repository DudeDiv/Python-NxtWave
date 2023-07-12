#Given the weekday of the first day of the month, determine the day of the week of the given date in that month.
D = input()
N = int(input())

if(D=="Sunday"):
    day=0
elif(D=="Monday"):
    day=1
elif(D=="Tuesday"):
    day=2
elif(D=="Wednesday"):
    day=3
elif(D=="Thursday"):
    day=4
elif(D=="Friday"):
    day=5
elif(D=="Saturday"):
    day=6

target_day = day+(N-1)
target_day = target_day%7

if(target_day==0):
    print("Sunday")
elif(target_day==1):
    print("Monday")
elif(target_day==2):
    print("Tuesday")
elif(target_day==3):
    print("Wednesday")
elif(target_day==4):
    print("Thursday")
elif(target_day==5):
    print("Friday")
elif(target_day==6):
    print("Saturday")
