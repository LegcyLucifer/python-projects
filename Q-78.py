l1 = ["java","python","php","c++","Rushik","mann","mital","ghanshyam","harsh","Gghanshyammm"]

max_length = max(len(word) for word in l1)

longest_words = [word for word in l1 if len(word) == max_length]

print(longest_words)

"""l2 = list(map(lambda value: value len(value)), l1)

max_value = max(l2)

print(max_value)
"""