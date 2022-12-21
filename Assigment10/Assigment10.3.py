from datetime import date, datetime
from khayyam import JalaliDate, jalali_datetime

class my_datetime:
    def __init__(self):
        self.my_date_HS = [1, 1, 1] # Hijri solar Calendar
        self.my_date_HS_month = 'farvardin'
        self.my_date_HL = [1, 1, 1] # Hijri lunar Calendar
        self.my_date_HL_month = 'muharram'
        self.my_date_Gr = [1, 1, 1] # Gregorian Calendar
        self.my_date_Gr_month = 'january'

    def Gregorian2HijriSolar(self, my_date):
        # my_date = [2022, 12, 20]
        ...
        
    def HijriSolar2Gregorian(self, my_date):
        ...
        
    def Gregorian2Hijrilunar(self, my_date):
        ...
        
    def Hijrilunar2Gregorian(self, my_date):
        ...

    def HijriSolar2Hijrilunar(self, my_date):
        ...

    def Hijrilunar2HijriSolar(self, my_date):
        ...

    def add_date(self, my_date, my_date2, date_type):
        ...

    def sub_date(self, my_date, my_date2, date_type):
        ...

    def get_month(self, num_month, date_type):
        # date_type = 'Gr' or 'HL' or 'HS'
        ...

    def get_Week_day(self, my_date, date_type):
        ...