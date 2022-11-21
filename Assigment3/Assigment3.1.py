import random

word_bank = ["book", "table", "char", "laptop", "Door", "Nastaran", "Mohammad", "sina", "akbar", "cow",\
 "Migration", "xiaomi", "Mohammad Saberian", "bad buys", "game over", "ferdowsi university of mashhad", "masshad mall"]

true_chars = []
fault_chars = []
user_mistakes = 0
incomplete = True

word = random.choice(word_bank)
word = word.lower()
for i in range(len(word)):
    if word[i] == " ":
        
        print(" ", end="")
    else:
        print("_ ", end="")

print(word)

while user_mistakes < 6:
    user_char = input("please write your guess: ").lower()

    if len(user_char) == 1:
        if user_char in true_chars or user_char in fault_chars:
            print("⚠ Don't enter repetitious")
            
        else:
            if user_char in word:
                true_chars.append(user_char)
                print("✅", end=" ")
            
            else:
                fault_chars.append(user_char)
                print("🈹", end=" ")
                user_mistakes += 1

        incomplete = False
        for i in range(len(word)):
            if word[i] == " ":
                print("  ", end="")
            elif word[i] in true_chars:
                print(word[i], end=" ")
            else:
                print("_ ", end="") 
                incomplete = True

        print(" || fault chars: ", end="")
        for i in range(len(fault_chars)):
            print(fault_chars[i], end=" - ")
        print("")

        if incomplete == False:
            print("🎉🎉 congratulation ** you win 👌🏻👌🏻")
            break

    else:
        print("⚠ Enter only 'one' character")

if user_mistakes == 6:
    print("game over 💀💀")