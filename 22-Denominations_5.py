#Write a program that reads an amount A and prints the minimum number of 2000, 500, 200, 50, 20, 5, 2 and 1 rupee notes required for the given amount.
A = int(input())
notes_2000 = int(A/2000)
notes_500 = int((A%2000)/500)
notes_200 = int(((A%2000)%500)/200)
notes_50 = int((((A%2000)%500)%200)/50)
notes_20 = int(((((A%2000)%500)%200)%50)/20)
notes_5 = int((((((A%2000)%500)%200)%50)%20)/5)
notes_2 = int(((((((A%2000)%500)%200)%50)%20)%5)/2)
notes_1 = int((((((((A%2000)%500)%200)%50)%20)%5)%2)/1)

print("2000:"+str(notes_2000)+" 500:"+str(notes_500)+" 200:"+str(notes_200)+" 50:"+str(notes_50)+" 20:"+str(notes_20)+" 5:"+str(notes_5)+" 2:"+str(notes_2)+" 1:"+str(notes_1))
