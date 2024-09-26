from first_task import *

data = read("data.txt")
serialize(data, "eedeeded.json")
show(data)

sorted_by_name = sort_by_name(data)
print("\nSorted by name:")
show(sorted_by_name)

sorted_by_cook_time = sort_by_cook_time(data)
print("\nSorted by cook time:")
show(sorted_by_cook_time)

sorted_by_price = sort_by_price(data)
print("\nSorted by price:")
show(sorted_by_price)