import random
choices = ["Rock","Paper","Scissors"]
computer = random.choice(choices)
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("Rock, Paper or Scissors?").capitalize()
    ## Codition of Rocker, Paper and Scissors
    if player == computer:
        print("tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You loose",computer, "covers", player)
            cpu_score +=1
        else:
            print("You win!", player, "smashes", computer)
            player_score+=1

    elif player ==  "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            cpu_score+=1
        else:
            print("You win!", player, "cover", computer)
            player_score+=1

    elif player == "Scissors":
        if computer == "Rock":
            print("You loose.....", computer, "smashes", player)
            cpu_score+=1
        else:
            print("you lose.....", computer, "smashes", player)
            cpu_score+=1
    elif player=='End':
        print("Final Scores:")
        print(f"CPU:{cpu_score}")
        print(f"Placer:{player_score}")
        break
