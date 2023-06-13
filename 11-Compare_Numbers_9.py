#Write a program that reads a three-digit number and checks if any of the below conditions is satisfied:
#Each digit of the given number is greater than 7.
#The product of any two digits is always less than or equal to 30.
A = input()
condition1 = A[0]>"7" and A[1]>"7" and A[2]>"7"
condition2 = ((int(A[0])*int(A[1])) <= 30) and ((int(A[1])*int(A[2])) <= 30) and ((int(A[2])*int(A[0])) <= 30)
print(condition1 or condition2)
