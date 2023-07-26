#Given a number N, write a program that reads N inputs and prints the greatest number among the given inputs.
N = int(input())
first_input = int(input())
greatest = first_input
for i in range(1,N):
    new_input = int(input())
    if(new_input>greatest):
        greatest = new_input
print(greatest)
