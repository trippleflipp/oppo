import json
import re
import datetime

import sorting

class Dish:
    def __init__(self, name: str, cook_time: datetime.time, price: float) -> None:
        self.name: str = name
        self.cook_time: datetime.time = cook_time
        self.price: float = price


    def read(txt_file: str) -> list:
        result = []

        with open(txt_file, "r") as file:
            lines = file.readlines()
            for line in lines:

                cook_time = re.findall("(?i)(\d?\d:\d\d)", line)[0]
                price = float(re.findall("\d+\.\d+", line)[0])
                name = re.findall('"(.+?)"', line)[0]

                new_dish = Dish(name, cook_time, price)
                result.append(new_dish)
        
        return result
    

    def serialize(dishes: list, output = None):
        to_dump = []

        for dish in dishes:
            to_dump.append({
                "name": dish.name,
                "cook_time": dish.cook_time,
                "price": dish.price
            })

        if output:
            with open(output, "w") as file:
                json.dump(to_dump, file)
                return
        return json.dumps(to_dump)
    

    def name_sort(dishes: list) -> list:
        return sorting.name_sort(dishes)
    

    def price_sort(dishes: list) -> list:
        return sorting.price_sort(dishes)
    

    def cook_time_sort(dishes: list) -> list:
        return sorting.cook_time_sort(dishes)
    
    
    def show(dishes: list) -> None:
        for dish in dishes:
            print(dish.name + ' ' + dish.cook_time + ' ' + str(dish.price))