#Given a string S, write a program to find the vowels in the given string S.
#Print the resultant string by joining all the vowels in the string S.
S = input()
string = ""
for i in S:
    if(i=="a"):
        string = string + "a"
    if(i=="e"):
        string = string + "e"
    if(i=="i"):
        string = string + "i"
    if(i=="o"):
        string = string + "o"
    if(i=="u"):
        string = string + "u"
print(string)
