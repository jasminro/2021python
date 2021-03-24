import random

name = input("Give your name: ")

while True:
    choice = int(input("Give your choice (1=rock, 2=paper, 3=scissors): "))
    # looping until user enter invalid input
    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))
          
    if choice == 1:
        choice_name = 'rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissors'
            
    comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissors'
            
    print(f"{name}: {choice_name} \nCPU: {comp_choice_name}")
  
    # condition for winning
    if (choice == comp_choice):
        result = "tie"
    
    elif ((choice == 1 and comp_choice == 2) or
      (choice == 2 and comp_choice ==1 )):
        result = "paper"
          
    elif((choice == 1 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)):
        result = "rock"
    else:
        result = "scissors"
  
    # Printing either user or computer wins
    if result == "tie":
        print("It's a tie")
    elif result == choice_name:
        print(f"{name} wins")
    else:
        print("CPU wins")

    while True:          
        print("Do you want to play again? (y/n)")
        ans = input().lower()
        if ans == 'n':
            print("You are weak!")
            exit()
        elif ans == 'y':
            break
        else:
            print("Invalid input!")
            continue