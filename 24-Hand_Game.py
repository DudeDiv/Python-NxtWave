#Write a program that reads two strings representing what Abhinav and Anjali showed and prints the winner of the game based on the shapes the players choose.
#Rock, Paper or Scissors
Abhinav = input()
Anjali = input()

if((Abhinav=="Paper" and Anjali=="Rock") or (Abhinav=="Rock" and Anjali=="Scissors") or (Abhinav=="Scissors" and Anjali=="Paper")):
    print("Abhinav Wins")
elif((Anjali=="Paper" and Abhinav=="Rock") or (Anjali=="Rock" and Abhinav=="Scissors") or (Anjali=="Scissors" and Abhinav=="Paper")):
    print("Anjali Wins")
else:
    print("Tie")
