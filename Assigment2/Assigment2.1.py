import random


cumputer_number = random.randint(10,40)
number_guess = 0

while True:
    user_number = int(input("entre your guess:"))
    number_guess = number_guess + 1

    if cumputer_number == user_number:
        print("you win 🎉🎉🎉")
        print("number guess: " + str(number_guess))
        break
    
    elif cumputer_number > user_number:
        print("go up ⏫")
        
    elif cumputer_number < user_number:
        print("go up ⏬")



        