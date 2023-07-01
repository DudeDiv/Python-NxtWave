#Write a program that reads a two-digit number N and checks if N is divisible by both the digits of N.
#Print the double of N if N is divisible by both the digits of N. Otherwise, print N.
N = input()
N_ = int(N)
N_0 = int(N[0])
N_1 = int(N[1])

if((N_%N_0==0) and (N_%N_1==0)):
    print(N_*2)
else:
    print(N_)
