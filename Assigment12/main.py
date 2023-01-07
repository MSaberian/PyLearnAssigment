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
        if 0 < choice < 9:
            if choice == 1:
                d.add()
            elif choice == 2:
                d.edit()
            elif choice == 3:
                UI().remove(d)
            elif choice == 4:
                UI.search(d)
            elif choice == 5:
                UI.show_list(d)
            elif choice == 6:
                print(d.number_media)
            elif choice == 7:
                ...
            elif choice == 8:
                d.write_to_database()
                exit(0)
        else:
            print('⚠ you have to enter number between 1-8')
    else:
        print('⚠ you have to enter number between 1-8')

# MEDIA[0].showinfo()
# MEDIA[1].showinfo()
# MEDIA[2].showinfo()
# d.show_list()
# d.search_index(2)
# d.add()
# print(d.media(4).name)
# print(d.media(4).director)
# print(d.media(4).IMDB_score)
# print(d.media(4).duration)
# d.media(4).showinfo()
# UI.remove(d)
# d.remove()
# d.show_list()
# UI.show_list(d)
# d.write_to_database()

