#Write a program that reads a word and prints the first two and the last two letters of the word
#and prints the stars (*) instead of the remaining letters.
word = input()
length = len(word)
print(word[:2]+("*"*(length-4))+word[length-2:])
