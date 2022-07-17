import random

score = 0
scorec = 0
while True:
    user_choice = input("Please select Rock (r), Paper (p) , Scissor (s) or Quit (q) : ").lower()
    comp_guess = random.randint(1,3)
    # print (comp_guess)
    if user_choice == 'q':
        print("Thank You for playing")
        break
    elif user_choice == 'r' and comp_guess == 3:
        print ("Computer chose Scissors.\nYou Won!")
        score += 1
    elif user_choice == 'p' and comp_guess == 1:
        print ("Computer chose Rock.\nYou Won!")
        score += 1
    elif user_choice == 's' and comp_guess == 2:
        print ("Computer chose Paper.\nYou Won!")
        score += 1
    elif user_choice == 'r' and comp_guess == 1:
        print ("DRAW!")
    elif user_choice == 'p' and comp_guess == 2:
        print ("DRAW!")
    elif user_choice == 's' and comp_guess == 3:
        print ("DRAW!")    
    else:
        print ("Computer Won!")
        scorec += 1

print ("Your Score was ", score)
print ("Computers Score was ", scorec)