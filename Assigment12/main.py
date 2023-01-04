from Media import Media
from Film import Film
from Series import Series
from Clip import Clip
from Documentary import Documentary
from Actor import Actor
from Database import Database
from UI import UI

d = Database()
MEDIA = d.read()

# MEDIA[0].showinfo()
# MEDIA[1].showinfo()
# MEDIA[2].showinfo()
# d.show_list()
# d.search_index(2)
d.add()
print(d.media(4).name)
print(d.media(4).director)
print(d.media(4).IMDB_score)
print(d.media(4).duration)
# d.media(4).showinfo()
# d.search(3)

