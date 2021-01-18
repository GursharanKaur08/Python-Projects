import random

# Game Design

game_parameters = ["rock","Paper","scissor"]
print("Welcome to our rock paper scissor game player software.")

user = input("Hey user , plz input your username : ")
user = user.upper()

user_score=0
computer_score=0
i=1
while i<=10:
    random_int = random.randint(0,2)
    print("Game show number : ",i)
    computer_entry = game_parameters[random_int]
    computer_entry = computer_entry.upper()
    user_entry = input(f"Hey {user}, Its your turn : ")
    user_entry = user_entry.upper()

    # condition check
    if (user_entry=="ROCK" and computer_entry=="SCISSOR") or (user_entry=="PAPER" and computer_entry=="ROCK") or (user_entry=="SCISSOR" and computer_entry=="PAPER"):
        print(f"congrats {user}, u get 10 points here.")
        user_score+=10
    elif (computer_entry=="ROCK" and user_entry=="SCISSOR") or (computer_entry=="PAPER" and user_entry=="ROCK") or (computer_entry=="SCISSOR" and user_entry=="PAPER"):
        print("OOPS! computer gets 10 points here.")
        computer_score+=10
    elif user_entry==computer_entry:
        print("No one get points here.")
    i+=1

# winner
print(f"{user} score : {user_score}")
print(f"Computer score : {computer_score}")

if user_score>computer_score:
    print("Congrats {user}, U won$$$$$.")
elif user_score<computer_score:
    print('OOps computer won, so try AGAIN!!')
else:
    print('GAME TIED, NICE TRY FROM BOTH SIDES.')
