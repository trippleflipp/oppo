from first_task import Dish

print('\nParsed data:')
data = Dish.read("test_data.txt")
Dish.serialize(data, "eedeeded.json")
Dish.show(data)

print('\nName sorting:')
sorted_data = Dish.name_sort(data)
Dish.show(sorted_data)

print('\nPrice sorting:')
sorted_data = Dish.price_sort(data)
Dish.show(sorted_data)

print('\nCook time sorting:')
sorted_data = Dish.cook_time_sort(data)
Dish.show(sorted_data)
