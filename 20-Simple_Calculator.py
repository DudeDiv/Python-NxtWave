#Write a program that reads an operator O, and two numbers A and B.
#Print the result by doing arithmetic operations on A and B based on the operator O
#Given operators: +, -, *, / and %.
O = input()
A = int(input())
B = int(input())

if(O=="+"):
    print(A+B)
elif(O=="-"):
    print(A-B)
elif(O=="*"):
    print(A*B)
elif(O=="/"):
    print(A/B)
elif(O=="%"):
    print(A%B)
