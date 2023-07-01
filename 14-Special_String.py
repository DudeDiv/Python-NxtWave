#Write a program that reads a string S and checks if all the given conditions are satisfied.
#The first three characters of S is NXT.
#The remaining characters of S contain a Number. Number is divisible by 2 or 7.
#Print Special String if all the given conditions are satisfied. Otherwise, print Not a Special String.
S = input()
nxt_part = S[0:3]
num_part = int(S[3:])
condition1 = nxt_part=="NXT"
condition2 = (num_part%2==0) or (num_part%7==0)

if(condition1 and condition2):
    print("Special String")
else:
    print("Not a Special String")
