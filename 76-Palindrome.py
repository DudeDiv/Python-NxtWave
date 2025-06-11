def is_Palindrome(s):
  return s[::-1].lower()==s.lower()

sample = input()
print(is_Palindrome(sample))
