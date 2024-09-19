import json
import re
import datetime

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
    

    def serialize(dishes, output = None):
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
    
    
    def show(dishes):
        for dish in dishes:
            print(dish.name + ' ' + dish.cook_time + ' ' + str(dish.price))


    def sort_by_name(dishes):
        return sorted(dishes, key=lambda dish: dish.name)

    def sort_by_cook_time(dishes):
        return sorted(dishes, key=lambda dish: dish.cook_time)


    def sort_by_price(dishes):
        return sorted(dishes, key=lambda dish: dish.price)

# Пример использования
data = Dish.read("test_data.txt")
Dish.serialize(data, "eedeeded.json")
Dish.show(data)

# Сортировка и вывод данных
sorted_by_name = Dish.sort_by_name(data)
print("\nSorted by name:")
Dish.show(sorted_by_name)

sorted_by_cook_time = Dish.sort_by_cook_time(data)
print("\nSorted by cook time:")
Dish.show(sorted_by_cook_time)

sorted_by_price = Dish.sort_by_price(data)
print("\nSorted by price:")
Dish.show(sorted_by_price)