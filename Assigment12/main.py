from Media import Media
from Film import Film
from Series import Series
from Clip import Clip
from Documentary import Documentary
from Actor import Actor
from Database import Database

d = Database()
MEDIA = d.read()
# MEDIA = Database().read()
# print(MEDIA[0].casts[0].name,MEDIA[0].casts[0].family)
# MEDIA[0].casts[1].dance()
MEDIA[0].showinfo()
MEDIA[1].showinfo()
MEDIA[2].showinfo()
# print(MEDIA[1].name)
# print(MEDIA[2].url[0])
