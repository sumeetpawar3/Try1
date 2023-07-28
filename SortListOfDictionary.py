my_list = [
    {'name': 'John', 'age': 25},
    {'name': 'Jane', 'age': 30},
    {'name': 'Bob', 'age': 20},
]

sorted_list = sorted(my_list, key=lambda x: x['age'])
print(sorted_list) 
