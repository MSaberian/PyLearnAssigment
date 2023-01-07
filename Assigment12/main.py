import time
from Media import Media
from Film import Film
from Series import Series
from Clip import Clip
from Documentary import Documentary
from Actor import Actor
from Database import Database
from UI import UI

print("welcome to MoSa MediaDataset")
print("Loading.",end='')
d = Database()
d.read()
for i in range(20):
    time.sleep(.1)
    print('.',end='')
print("\nData is loaded.")

while True:
    UI.show_menu()
    choice_user = input("enter your choice: ")
    if choice_user.isdigit():
        choice = int(choice_user)
        if 0 < choice < 8:
            if choice == 1:
                d.add()
            elif choice == 2:
                d.edit()
            elif choice == 3:
                UI.remove(d)
            elif choice == 4:
                UI.search(d)
            elif choice == 5:
                UI.show_list(d)
            elif choice == 6:
                UI.download(d)
            elif choice == 7:
                d.write_to_database()
                exit(0)
        else:
            print('⚠ you have to enter number between 1-7')
    else:
        print('⚠ you have to enter number between 1-7')
