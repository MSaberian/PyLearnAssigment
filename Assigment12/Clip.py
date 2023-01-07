from Media import Media

class Clip(Media):
    def __init__(self,name,director,IMDB_cvore,duration):
        super().__init__(name,director,IMDB_cvore,duration)
        self.production_year = ...
        self.type = 'clip'

    def showinfo(self):
        print('\n *** ### ***\n')
        print(self.name,'is a',self.production_year,self.type,'directed by',self.director)
        self.showinfoHiden()

    # def download(self):
    #     ...
