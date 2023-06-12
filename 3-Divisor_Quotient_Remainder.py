#Write a program that reads a dividend and a divisor and prints the remainder.
dividend = int(input())
divisor = int(input())
quotient = int(dividend/divisor)
remainder = dividend - (divisor * quotient)
print(remainder)

#ALTERNATE CODE
#dividend = int(input())
#divisor = int(input())
#quotient = dividend // divisor
#remainder = dividend % divisor
#print(remainder)
