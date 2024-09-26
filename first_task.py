import json
import re
import datetime
import logging

class Dish:
    def __init__(self, name: str, cook_time: datetime.time, price: float) -> None:
        self.name: str = name
        self.cook_time: datetime.time = cook_time
        self.price: float = price


def read_name(line: str) -> str:
    name = ""
    try:
        name = re.findall('"(.+?)"', line)[0]
    except:
        logging.error("Reading name error")
    return name


def read_price(line: str) -> float:
    variants = line.split(' ')
    for variant in variants:
        if ":" in variant:
            continue
        try:
            return float(variant)
        except:
            continue
    logging.error("There is no price :(")
    return 0


def read_cook_time(line: str) -> str:
    cook_time = re.findall(r"(?i)(\d?\d?:\d?\d?)", line)[0]
    if len(cook_time) < 5:
        logging.error("Stop using incorrect time...")
    s = cook_time.split(":")
    if len(s[0]) < 2:
        s[0] = '0' + s[0]
    if len(s[1]) < 2:
        s[1] = s[1] + '0'
    return s[0] + ':' + s[1]


def read(txt_file: str) -> list:
    result = []

    with open(txt_file, "r") as file:
        lines = file.readlines()
        for line in lines:

            cook_time = read_cook_time(line)
            price = read_price(line)
            name = read_name(line)

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


def sort_by_name(dishes):
    return sorted(dishes, key=lambda dish: dish.name)


def sort_by_cook_time(dishes):
    return sorted(dishes, key=lambda dish: dish.cook_time)


def sort_by_price(dishes):
    return sorted(dishes, key=lambda dish: dish.price)


def show(dishes: list) -> None:
    for dish in dishes:
        print(dish.name + ' ' + dish.cook_time + ' ' + str(dish.price))