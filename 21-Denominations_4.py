#Write a program that reads an amount A and prints the minimum number of 100, 50, 20 and 10 rupee notes required for the given amount.
A = int(input())
notes_100 = int(A/100)
notes_50 = int((A%100)/50)
notes_20 = int(((A%100)%50)/20)
notes_10 = int((((A%100)%50)%20)/10)

print("100 Notes:",notes_100)
print("50 Notes:",notes_50)
print("20 Notes:",notes_20)
print("10 Notes:",notes_10)
