#Given a sentence S. Write a program to emove all the vowels in the given sentence.
word = input()
vowels = "aeiouAEIOU"
for i in vowels:
  word = word.replace(i,"")
print(word)
