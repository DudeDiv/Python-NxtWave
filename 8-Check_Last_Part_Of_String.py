#Write a program that reads two words A and B and checks if the second word B
#is the last part of the first word A.
word1 = input()
word2 = input()
word_1 = len(word1)
word_2 = len(word2)
word_diff = word_1 - word_2
print(word2==word1[word_diff:])
