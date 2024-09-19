from first_task import Dish

data = Dish.read("test_data.txt")
Dish.serialize(data, "eedeeded.json")
Dish.show(data)

sorted_by_name = Dish.sort_by_name(data)
print("\nSorted by name:")
Dish.show(sorted_by_name)

sorted_by_cook_time = Dish.sort_by_cook_time(data)
print("\nSorted by cook time:")
Dish.show(sorted_by_cook_time)

sorted_by_price = Dish.sort_by_price(data)
print("\nSorted by price:")
Dish.show(sorted_by_price)