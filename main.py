class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name=name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print(self.name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print("Ресторан открыт")

    def reit(self, reit):
        self.reit=reit
        print(self.reit)

spisok=["шоколадное", "ванильное", "крем-брюле", "фисташковое"]

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type, mesto, vremya):
        self.name = name
        self.cuisine_type = cuisine_type
        self.mesto = mesto
        self.vremya = vremya

    def describe_restaurant(self):
        print(self.name)
        print(self.cuisine_type)
        print(self.mesto)
        print(self.vremya)


class myagkoe(IceCreamStand):
    def sort(self):
        self.flavors=spisok
        print(self.flavors)

    spisok = ["шоколадное", "ванильное", "крем-брюле", "фисташковое"]
    def dobav(self):
        a=str(input())
        spisok.append(a)
        print(spisok)

    def delete(self):
        print("Какой сорт удалить?")
        a=str(input())
        spisok.remove(a)
        print(spisok)

    def proverka(self):
        print("Какой сорт хотите проверить?")
        a=str(input())
        if a in spisok:
            print("Есть в наличии")
        else:
            print("Нету")


class napalochke(IceCreamStand):
    def sort(self):
        self.flavors=spisok
        print(self.flavors)

    spisok = ["шоколадное", "ванильное", "крем-брюле", "фисташковое"]
    def dobav(self):
        a=str(input())
        spisok.append(a)
        print(spisok)

    def delete(self):
        print("Какой сорт удалить?")
        a=str(input())
        spisok.remove(a)
        print(spisok)

    def proverka(self):
        print("Какой сорт хотите проверить?")
        a=str(input())
        if a in spisok:
            print("Есть в наличии")
        else:
            print("Нету")


IceCream=napalochke("Ши", "cuisine", "ss", "d")
IceCream.describe_restaurant()
IceCream.sort()
IceCream.proverka()
