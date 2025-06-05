# Without using get and set

from typing import Any


class Car:
    def __init__(self):
        self.brand = {}

    def add_detail(self, brand, date):
        self.brand[brand] = date

    def check_date(self, brand):
        if brand in self.brand:
            print(self.brand[brand])

        else:
            print("No record found")


car1 = Car()
car1.add_detail("Toyota", 2021)

car1.check_date("Toyota")

# Using get and set


class Airplane:
    def __init__(self):
        self.model = {}

    def __setitem__(self, key, value):
        self.model[key] = value

    def __getitem__(self, item):
        return self.model[item]


a1 = Airplane()

a1["airblue"] = 2018
print(a1["airblue"])