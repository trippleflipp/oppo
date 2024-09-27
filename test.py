from first_task import *

data = read(txt_file="test_data.txt")

def test_dish_name_read():
    assert read_name('03:22 12.3 "') == ''

def test_dish_price_read():
    assert read_price('"Pelmeni" 00:30 22') == 22.0

def test_dish_cook_time_read():
    assert read_cook_time('3.3 "Pizza" 2:4') == "02:04"

def test_data_read():
    read(txt_file="test_data.txt")

def test_serialize():
    serialize(data)

def test_sort_by_name():
    sort_by_name(data)

def test_show():
    show(data)
