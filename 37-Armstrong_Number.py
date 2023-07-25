#Write a program that reads a number N and checks if N is an Armstrong Number.
#Print Armstrong Number if the given number is an Armstrong Number. Otherwise, print Not an Armstrong Number.
N = input()
sum = 0
for i in N:
    sum = sum + int(i)**len(N)
if(str(sum)==N):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
