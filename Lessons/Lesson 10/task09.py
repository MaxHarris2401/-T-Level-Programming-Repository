thisdict = {'b': 2, 'a': 1, 'c': 3}
sorted_list = sorted(thisdict.items())

sorted_dict = {}
for key, value in sorted_list:
    sorted_dict[key] = value

print(sorted_dict)