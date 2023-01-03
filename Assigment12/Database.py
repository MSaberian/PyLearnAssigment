from Media import Media
from Film import Film
from Series import Series
from Clip import Clip
from Documentary import Documentary
from Actor import Actor

class Database:
    def __init__(self, path="media_database.txt"):
        self.path = path

    def read(self):
        f = open(self.path,"r")
        line_number = 0
        MEDIA = []
        
        for line in f:
            line_number += 1
            line = line.replace('\n', '')
            result = line.split(",")
            if line[0] == '@':
                new_media.Actor = ACTORS
                MEDIA.append(new_media)
                line_number = 0
                
            if line_number == 1:
                Type_media = result[0]
                ACTORS = []
                if Type_media == 'S':
                    new_media = Series(result[1],result[2],result[3],result[4])
                    new_media.number_episodes = result[5]
                    new_media.number_season = result[6]
                    new_media.start_year = result[7]
                    new_media.end_year = result[8]
                    new_media.Finished = result[9]
                elif Type_media == 'F':
                    new_media = Film(result[1],result[2],result[3],result[4])
                    new_media.production_year = result[5]
            elif line_number == 2:
                new_media.country = result
            elif line_number == 3:
                new_media.genre = result
            elif line_number == 4:
                new_media.url = result
            elif line_number > 4:
                new_actor = Actor(result[0],result[1],result[2],result[3])           
                ACTORS.append(new_actor)

        f.close()
        return MEDIA

    def write(self):
        open('media_database.txt', 'w').close()
        file_object = open('media_database.txt', 'a')
        # for product in PRODUCTS:
        #     file_object.write(str(product["code"])+","+str(product['name'])+','+str(product['price'])+','+str(product['count'])+'\n')
        file_object.close()

# d = Database()
# MEDIA = d.read()
# # MEDIA = Database().read()
# print(MEDIA[0].Actor[0].name)
# print(MEDIA[1].name)
# print(MEDIA[2].url[0])