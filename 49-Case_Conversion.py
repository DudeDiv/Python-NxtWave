#Given a string, write a program to modify the string as given below.
#Add a sapce before each uppercase character excluding the first uppercase character.
#Print the modified string.
word = input()
result = "" #Or result = word[0]
for i in range(1,len(word)):
    if(word[i]==word[i].upper()):
        result = result + " " + word[i]
    else:
        result = result + word[i]
result = word[0]+result
print(result)
