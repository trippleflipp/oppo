def name_sort(data: list):
    return sorted(data, key=lambda dish: dish.name)

def price_sort(data: list):
    return sorted(data, key=lambda dish: dish.price)

def cook_time_sort(data: list):
    return sorted(data, key=lambda dish: dish.cook_time)