from Media import Media
from Film import Film
from Series import Series
from Clip import Clip
from Documentary import Documentary
from Actor import Actor

class Database:
    def __init__(self, path="media_database.txt"):
        self.path = path
        self.Media = ...
        self.number_media = ...

    def read(self):
        f = open(self.path,"r")
        line_number = 0
        index = 0
        MEDIA = []
        
        for line in f:
            line_number += 1
            line = line.replace('\n', '')
            result = line.split(",")
            if line[0] == '@':
                index += 1
                new_media.index = index
                new_media.casts = ACTORS
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
                elif Type_media == 'D':
                    new_media = Documentary(result[1],result[2],result[3],result[4])
                    new_media.production_year = result[5]
                elif Type_media == 'C':
                    new_media = Clip(result[1],result[2],result[3],result[4])
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
        self.number_media = index
        self.Media =  MEDIA
        return MEDIA
    
    def write_to_database(self): 
        open(self.path, 'w').close()
        file_object = open(self.path, 'a')
        temp_string = ''
        for media in self.Media:
            typemedia = media.type.capitalize()[0]
            temp_string += typemedia + ',' + media.name + ',' + media.director + ',' + media.IMDB_score + ',' + media.duration + ','
            if media.type == 'series':
                temp_string += media.number_episodes + ',' + media.number_season + ',' + media.start_year + ',' + media.end_year + ',' + media.Finished
            elif media.type == 'film':
                temp_string += media.production_year
            elif media.type == 'documentary':
                temp_string += media.production_year
            elif media.type == 'clip':
                temp_string += media.production_year
            temp_string += '\n' 
            for i in range(len(media.country)-1):
                temp_string += media.country[i] + ','
            temp_string += media.country[-1] 
            temp_string += '\n' 
            for i in range(len(media.genre)-1):
                temp_string += media.genre[i] + ','
            temp_string += media.genre[-1] 
            temp_string += '\n' + media.url[0]
            for actor in media.casts:
                temp_string += '\n' + actor.name + ',' + actor.family + ',' + actor.year_birth + ',' + actor.sex
            temp_string += '\n@'
            file_object.write(temp_string)
            temp_string = '\n'
        file_object.close()

    def add(self):
        print("To add new media, please complete the following parameters.")
        print("In first enter type of media:")
        print("1- film      2- series   3- documentry   4- clip")
        type_medai = int(input("enter your choice: "))
        name = input("enter name: ")
        director = input("enter director: ")
        IMDB_score = input("enter IMDB score: ")
        IMDB_duration = input("enter duration: ")
        if type_medai == 1:
            new_media = Film(name,director,IMDB_score,IMDB_duration)
            new_media.production_year = input("enter production year: ")
            new_media.type = 'film'
        elif type_medai == 2:
            new_media = Series(name,director,IMDB_score,IMDB_duration)
            new_media.number_episodes = input("enter number episodes: ")
            new_media.number_season = input("enter number season: ")
            new_media.start_year = input("enter start year: ")
            new_media.end_year = input("enter end year: ")
            new_media.Finished = input("enter Finished: ")
            new_media.type = 'series'
        elif type_medai == 3:
            new_media = Documentary(name,director,IMDB_score,IMDB_duration)
            new_media.production_year = input("enter production year: ")
            new_media.type = 'documentary'
        else:
            new_media = Clip(name,director,IMDB_score,IMDB_duration)
            new_media.production_year = input("enter production year: ")
            new_media.type = 'clip'
        countries = input("enter countries name with \",\" between them: ")
        new_media.country = countries.split(",")
        genres = input("enter genres with \",\" between them: ")
        new_media.genre = countries.split(",")
        links = input("enter download links with \",\" between them: ")
        new_media.url = links.split(",")
        print('enter actors information.')
        while True:
            name = input("enter name actor: ")
            family = input("enter family actor: ")
            year_birth = input("enter year birth actor: ")
            sex = input("enter actor sex: ")
            new_actor = Actor(name, family, year_birth, sex)
            new_media.casts.append(new_actor)
            answer_user = input('do you want add new actor or finish? enter y (to yes) or n (to no): ')
            if answer_user == 'n':
                break
        new_media.index = self.number_media + 1
        self.Media.append(new_media)
        self.number_media += 1

    def edit(self):
        user_input = input("enter your index: ")
        index = int(user_input)
        if 0 < index <= self.number_media:
            Medias = self.Media
            print(index,'-',Medias[index-1].name)
            print("Which item do you want to change?")
            print("1- Name      2- director     3- IMDB_score")
            user_choice = int(input("your choice: "))
            if user_choice == 1:
                new_name = input('New name: ')
                Medias[index-1].name = new_name
            elif user_choice == 2:
                new_director = input('New director: ')
                Medias[index-1].director = new_director
            elif user_choice == 3:
                new_IMDB_score = input('New IMDB_score: ')
                Medias[index-1].IMDB_score = new_IMDB_score
            print('Data changed successfully')

                
        else:
            print("not found")

    def media(self,index):
        return self.Media[index-1]

    def remove(self,index):
        self.Media.pop(index)
        for i in range(self.number_media-1):
            self.media(i+1).index = i + 1

    def search_name(self,sabject):
        for media in self.Media:
            if sabject.lower() in media.name.lower():
                media.showinfo()

    def search_index(self,sabject):
        Medias = self.Media
        if type(sabject) == int:
            index = int(sabject)
            if 0 < index <= self.number_media:
                Medias[index-1].showinfo()

    def search_duration(self,duration1,duration2):
        for media in self.Media:
            if duration1 <= int(media.duration) <= duration2:
                media.showinfo()

    def download(self,index):
        Medias = self.Media
        if 0 < index <= self.number_media:
            print(Medias[index-1].name + 'is downloading, this may take several minutes')
            Medias[index-1].download()

    def dancing(self,index):
        Medias = self.Media
        if 0 < index <= self.number_media:
            for actor in self.media(index).casts:
                print(actor.name)
                actor.dance()