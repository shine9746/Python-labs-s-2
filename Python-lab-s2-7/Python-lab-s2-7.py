#python programme to print key,value,items of dictionary
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

key = list(dict_num.keys())
key = str(key)[1:-1]

value = list(dict_num.values())
value = str(value)[1:-1]

items = list(dict_num.items())
items = str(items)[1:-1]

print("key   :",key)

print("value :",value)

print("items :",items)

