#Given two integers M and N, write a program to prin a solid rectangle pattern of M rows and N columns using the asterisk character(*).
M = int(input())
N = int(input())
i = 0
while (i<M):
    print("* "*N)
    i = i+1
