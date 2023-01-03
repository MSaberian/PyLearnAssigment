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
print(MEDIA[0].Actor[0].name,MEDIA[0].Actor[0].family)
MEDIA[0].Actor[1].dance()
print(MEDIA[1].name)
print(MEDIA[2].url[0])
