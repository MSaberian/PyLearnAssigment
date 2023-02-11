import pyfiglet
import random
import time
from colorama import Fore
from colorama import Style


title = pyfiglet.figlet_format("TicTacToe",font="standard")
print(title)

player1_points = []
player2_points = []
CPU_number = -1

def show():
    for row in range(3):
        for col in range(3):
            if [row,col] in player1_points:
                print(f"{Fore.RED}X{Style.RESET_ALL}", end=" ")
            elif [row,col] in player2_points:
                print(f"{Fore.BLUE}O{Style.RESET_ALL}", end=" ")
            else:
                print("-", end=" ")
        print()    

def get_point(player_points, player_name):
    while True:
        if player_name == "CPU player":
            row = random.randint(0, 2)
            col = random.randint(0, 2)
        else:
            row = int(input("row: "))
            col = int(input("col: "))

        if 0 <= row <= 2 and 0 <= col <= 2:
            if not [row,col] in player1_points and not [row,col] in player2_points:
                player_points.append([row,col])
                break
            elif player_name != "CPU player":
                print("⚠ Don't enter repation point")
        else:
            print("⚠ you have to enter numbers between 0-2")

def check_game(player_points, player_name):
    sum2 = 0
    sum3 = 0
    for i in range(3):
        sum0 = 0
        sum1 = 0
        for j in range(3):
            if [i,j] in player_points:
                sum0 += 1
            if [j,i] in player_points:
                sum1 += 1

        if [i,i] in player_points:
            sum2 += 1
        if [i,2-i] in player_points:
            sum3 += 1
        
        if sum0 == 3 or sum1 == 3 or sum2 == 3 or sum3 == 3:
            print("\n\n *** ", player_name," win 🎉🎉👌🏻 ***\n\n")
            return True
    
    return False

def play(NumPlayer):
    if NumPlayer == 0:
        if CPU_number == -1:
            player_name = "player 1"
        elif CPU_number == 0:
            player_name = "CPU player"
        elif CPU_number == 1:
            player_name = "real player"
        player_points_play = player1_points
    else:
        if CPU_number == -1:
            player_name = "player 2"
        elif CPU_number == 0:
            player_name = "real player"
        elif CPU_number == 1:
            player_name = "CPU player"
        player_points_play = player2_points

    print(player_name)
    get_point(player_points_play, player_name)
    show()
    return check_game(player_points_play, player_name)
    
print("""please define play vs CPU or vs another player?
0: player vs player
1: player vs CPU""")

starttime = time.time()

while True:
    play_vs = int(input("your choice: "))
    if play_vs == 0 or play_vs == 1:
        break
    else:
        print("⚠ you have to enter numbers 0 or 1")


if play_vs:
    CPU_number = random.randint(0, 1)
    print("CPU player number: ", str(CPU_number))

show()

counter = -1
while True:
    counter += 1
    if play(counter%2):
        break
    elif counter == 8:
        print("\n*** Game have no winer ***")
        break

endtime = time.time()
print("Time Taken for this game is:", round(endtime - starttime, 2), "\n")