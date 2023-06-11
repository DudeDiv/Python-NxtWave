#Write a program that reads a word W, an index I, and a letter C.
#Print the word W by replacing the letter at the index I with the given letter C.
W = input()
I = int(input())
C = input()
print(W[:I]+C+W[I+1:])
