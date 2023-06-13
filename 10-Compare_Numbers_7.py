#Writea program that reads a four-digit number and checks if the first two digits of the number
#is 19 and the last two digits of the number is between 30 and 60.
A = input()
condition1 = A[:2]=="19"
condition2 = int(A[2:4])>30 and int(A[2:4])<60
print(condition1 and condition2)
