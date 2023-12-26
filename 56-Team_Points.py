#Write a function with the name calculate_league_points that takes the number of wins, draws, and losses and calculates the number of points a football team has obtained so far.
#-Each win is equal to 4 points
#-Each draw is equal to 2 points
#-Each loss is equal to -1 point
def calculate_league_points(wins, draws, losses):
    total = (wins*4) + (draws*2) - (losses*1)
    return total

statistics = input().split(",")
wins = int(statistics[0])
draws = int(statistics[1])
losses = int(statistics[2])
result = calculate_league_points(wins,draws,losses)
print(result)
