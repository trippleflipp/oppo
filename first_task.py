import datetime
import re

dishes = []

class Dish:
    def __init__(self, name: str, cook_time: str, price: float) -> None:
        self.name: str = name
        self.cook_time: str = cook_time
        self.price: float = price
        

with open("test_data.txt", "r") as file:
    data = file.readlines()
    for dish in data:

        cook_time = re.findall("(?i)(\d?\d:\d\d)", dish)
        price = re.findall("\d+\.\d+", dish)
        name = re.findall('"(.+?)"', dish)

        new_dish = Dish(name[0], cook_time[0], float(price[0]))
        dishes.append(new_dish)


print("Менюшечка:\n")
for dish in dishes:
    print(dish.name + ' ' + str(dish.price) + ' ' + dish.cook_time)