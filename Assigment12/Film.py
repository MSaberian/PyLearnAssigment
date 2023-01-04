from Media import Media

class Film(Media):
    def __init__(self,name,director,IMDB_score,duration):
        super().__init__(name,director,IMDB_score,duration)
        self.production_year = ...
        self.type = 'film'
        # self.season = ...

    def showinfo(self):
        print('\n *** ### ***\n')
        print(self.name,'is a',self.production_year,self.type,'directed by',self.director)
        self.showinfoHiden()

    # def download(self):
    #     ...
