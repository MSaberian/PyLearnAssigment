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
    def show_list(Medias):
        for i in range(len(Medias)):
            print(i+1,'-',Medias[i].name)


    