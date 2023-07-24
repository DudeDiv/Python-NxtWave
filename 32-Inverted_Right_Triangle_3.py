#Write a program that reads a number N and prints an Inverted Right Angled Triangle of N rows using stars(*) and pluses(+).
#The first row contains N stars (*) and the next N-1 rows contains pluses(+).
N = int(input())
i = N
while(i>0):
    if(i==N):
        print("* " * N)
    else:
        print("+ " * i)
    i = i-1
