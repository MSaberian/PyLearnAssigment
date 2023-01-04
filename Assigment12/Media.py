class Media:
    def __init__(self,name,director,IMDB_score,duration):
        self.name = name
        self.director = director
        self.IMDB_score = IMDB_score
        self.url = ...
        self.duration = duration
        self.casts = ...
        self.genre = ...
        self.country = ...
        self.type = ...
        self.index = ...

    def showinfoHiden(self):
        print('IMDB score:',self.IMDB_score)
        print('duration:',self.duration,'minutes')
        print('country:', end=' ')
        for i in range(len(self.country)-1):
            print(self.country[i], end=', ')
        print(self.country[-1]) 
        print('genre:', end=' ')
        for i in range(len(self.genre)-1):
            print(self.genre[i], end=', ')
        print(self.genre[-1])      
        print('Link download:',self.url[0])
        print('Actors:')
        for i in range(len(self.casts)):
            print(self.casts[i].name,self.casts[i].family,'is a',self.casts[i].sex,'that was born in',self.casts[i].year_birth)


    def download(self):
        ...
