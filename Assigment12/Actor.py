class Actor:
    def __init__(self,name,family,year_birth,sex):
        self.name = name
        self.family = family
        self.year_birth = year_birth
        self.sex = sex

    def dance(self):
        if self.sex == 'female':
            print('ππ»ππ»ππ»')
        elif self.sex == 'bisexual':
            print('π€·π»ββοΈπ€¦π»ββοΈπ€·π»ββοΈ')
        else:
            print('πΊπ»πΊπ»πΊπ»')
