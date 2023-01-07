from Media import Media

class Documentary(Media):
    def __init__(self,name,director,IMDB_cvore,duration):
        super().__init__(name,director,IMDB_cvore,duration)
        self.production_year = ...
        self.type = 'documentary'

    def showinfo(self):
        print('\n *** ### ***\n')
        print(self.name,'is a',self.production_year,self.type,'directed by',self.director)
        self.showinfoHiden()
