from datetime import date

class Student:

    def __init__(self, ID, N, DOB, C):
        self.__ID = ID
        self.__name = N
        self.__DOB = DOB
        self.__classification = C

    def current_age(self):
        today = date.today()
        #today = today.split("-")
        #self.__DOB = self.__DOB.split("-")
        age = today.year - self.__DOB.year
        print(f'({self.__name} is {age} years old')

    def registration_dates(self):
        if self.__classification == 'Sr':
            print(f'{self.__name} can register from 11/1 thru 11/3')
        elif self.__classification == 'Jr':
            print(f"{self.__name} can register from 11/4 thru 11/6")
        elif self.__classification == 'S':
            print(f"{self.__name} can register from 11/7 thru 11/9")
        elif self.__classification == 'F':
            print(f"{self.__name} can registerfrom 11/10 thru 11/12")
        else:
            print("The student cannot register")

    def get_DOB(self):
        return self.__DOB
    
    