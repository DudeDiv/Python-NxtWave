#Given a character C, write a program to check if the C is a Lowercase letter or Uppercase Letter or Digit or a Special Character.
C = input()
if C.isdigit():
    print("Digit")
elif(C==C.lower() and C==C.upper()):
    print("Special Character")
elif(C==C.lower()):
    print("Lowercase Letter")
elif(C==C.upper()):
    print("Uppercase Letter")
