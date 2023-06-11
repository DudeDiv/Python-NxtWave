#Write a program that reads a word and a number N and prints the last N characters of the word.
word = input()
num = int(input())
length = len(word)
reqd = length - num
print(word[reqd:])
