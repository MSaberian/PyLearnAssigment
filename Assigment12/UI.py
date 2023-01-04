from Media import Media
from Film import Film
from Series import Series
from Clip import Clip
from Documentary import Documentary
from Actor import Actor
from Database import Database

class UI():
    def __init__(self):
        ...

    @staticmethod
    def remove(database):
        user_input = input("enter your index you want to remove: ")
        index = int(user_input)
        if 0 < index <= database.number_media:
            database.remove(index)

    @staticmethod
    def show_list(database):
        Medias = database.Media
        for media in Medias:
            print(media.index,'-',media.name)

    @staticmethod
    def show_menu():
        print("1- Add")
        print("2- Edit")
        print("3- Remove")
        print("4- Search")
        print("5- Show List")
        print("6- Buy")
        print("7- Creat Qr Code")
        print("8- Exit")

    @staticmethod
    def search(database):
        print("Do you want search index or name?")
        print("1- index      2- name  ")
        user_choice = int(input('your choice: '))
        if user_choice == 1:
            user_choice = int(input('your search index: '))
            database.search_index(user_choice)
        else:
            user_choice = input('your search name: ')
            database.search_name(user_choice)



    # while True:
    #     show_menu()
    #     choice_user = input("enter your choice: ")
    #     if choice_user.isdigit():
    #         choice = int(choice_user)
    #         if 0 < choice < 9:
    #             if choice == 1:
    #                 add()
    #             elif choice == 2:
    #                 edit()
    #             elif choice == 3:
    #                 remove()
    #             elif choice == 4:
    #                 search()
    #             elif choice == 5:
    #                 show_list()
    #             elif choice == 6:
    #                 buy()
    #             elif choice == 7:
    #                 qrcode0()
    #             elif choice == 8:
    #                 write_to_database()
    #                 exit(0)
    #         else:
    #             print('⚠ you have to enter number between 1-8')
    #     else:
    #         print('⚠ you have to enter number between 1-8')
        