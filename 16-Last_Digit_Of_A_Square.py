#Write a program that reads a number N and checks if the last digit of N is equal to the last digit of the square of N.
#Print Equal if the last digit of N is equal to the last digit of the square of N. Otherwise, print Not Equal.
N = int(input())
N_sq = N**2
N_str = str(N)
N_sq_str = str(N_sq)
N_str_length = len(N_str)
n_sq_str_length = len(N_sq_str)

if((N_str[N_str_length-1:])==N_sq_str[n_sq_str_length-1:]):
    print("Equal")
else:
    print("Not Equal")
