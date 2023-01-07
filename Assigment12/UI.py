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
        print("6- download")
        print("7- dancing")
        print("8- Exit")

    @staticmethod
    def search(database):
        print("Do you want search index or name?")
        print("1- index      2- name    3- duration")
        user_choice = int(input('your choice: '))
        if user_choice == 1:
            user_choice = int(input('your search index: '))
            database.search_index(user_choice)
        elif user_choice == 2:
            user_choice = input('your search name: ')
            database.search_name(user_choice)
        elif user_choice == 3:
            user_choice1 = int(input('your search duration 1: '))
            user_choice2 = int(input('your search duration 2: '))
            database.search_duration(user_choice1,user_choice2)

    @staticmethod
    def remove(database):
        user_choice = int(input('your media index to remove: '))
        database.remove(user_choice-1)
        
    @staticmethod
    def download(database):
        user_choice = int(input('your media index to download: '))
        database.download(user_choice)

    @staticmethod
    def dancing(database):
        user_choice = int(input('your media index that you want to this actors dance for you: '))
        database.dancing(user_choice)