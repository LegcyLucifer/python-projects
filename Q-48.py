my_dict = {'apple': 10, 'banana': 3, 'cherry': 7, 'date': 5}

ascending_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]))

descending_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Original dictionary:", my_dict)
print("Ascending order by value:", ascending_sorted)
print("Descending order by value:", descending_sorted)