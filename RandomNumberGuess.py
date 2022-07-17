import random

max = int (input ("Enter the maximum for the range of the Number: \n"))

comp_guess = random.randint(1,max+1)
times = 1
while True:
    user_guess = int(input ("Please Guess the correct number: "))
    
    if user_guess > comp_guess:
        print ("Your guess is greater than the number.")
    elif user_guess < comp_guess:
        print ("Your guess is lower than the number.")
    else:
        print ("Your Guess is Correct!!")
        break
    times += 1

print (f"You took {times} tries to guess the correct answer")
hiscore = 100
if hiscore > times:
    with open ("hiscore.txt", 'w') as f:
        print ("You broke the HiScore!")
        f.write(times)
with open ("hiscore.txt") as f:
    hiscore = f.read("hiscore.txt")