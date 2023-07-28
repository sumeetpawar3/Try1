list_1 = [2, 6, 7, 3]
list_2 = [1, 4, 2]

list_3 = [ x+y for x in list_1 for y in list_2 ]

print(list_3)
print("Added elements")