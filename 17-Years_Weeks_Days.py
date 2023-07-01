#Given N number of days as input, write a program to convert N number of days to years (Y), weeks (W) and days (D).
N = int(input())
Y = int(N/365)
days_left = N-(365*Y)
W = int(days_left/7)
D = int(days_left%7)
print(Y)
print(W)
print(D)
