from Media import Media

class Series(Media):
    def __init__(self,name,director,IMDB_cvore,duration):
        super().__init__(name,director,IMDB_cvore,duration)
        self.type = 'series'
        self.number_episodes = ...
        self.number_season = ...
        self.start_year = ...
        self.end_year = ...
        self.Finished = ...

    def showinfo(self):
        print('\n *** ### ***\n')
        print(self.name,'is a',self.type,'directed by',self.director,'.')
        print('This series is product in',self.number_episodes,'episodes on',self.number_season,'season',end='. ')
        if self.Finished == 'True':
            print('And showed between',self.start_year,'and',self.end_year,'.')
        else:
            print('And it has been shown since',self.start_year,'and continues.')
        self.showinfoHiden()

    # def download(self):
    #     ...
