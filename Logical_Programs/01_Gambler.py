import random

stake = int(input("Enter stake: "))
goal = int(input("Enter goal: "))
trials = int(input("Enter number of trials: "))

wins = 0
bets = 0

for i in range(trials):

    cash = stake

    while cash > 0 and cash < goal:
        bets += 1

        if random.random() < 0.5:
            cash += 1
        else:
            cash -= 1

    if cash == goal:
        wins += 1

print("Wins:", wins)
print("Win %:", (wins/trials)*100)
print("Loss %:", 100 - (wins/trials)*100)