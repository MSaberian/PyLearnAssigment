class Actor:
    def __init__(self,name,family,year_birth,sex):
        self.name = name
        self.family = family
        self.year_birth = year_birth
        self.sex = sex

    def dance(self):
        if self.sex == 'f':
            print('💃🏻💃🏻💃🏻')
        else:
            print('🤷🏻‍♂️🤦🏻‍♂️🤷🏻‍♂️')

    # def download(self):
    #     ...
