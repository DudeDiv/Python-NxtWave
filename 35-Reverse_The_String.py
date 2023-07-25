#Write a program to print the reverse of the given string.
S = input()
string = ""
for i in range(0,len(S)):
    string = string + S[len(S)-1-i]
print(string)
