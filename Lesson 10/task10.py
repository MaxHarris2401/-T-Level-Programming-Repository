d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
for key in d2 and d1:
    if key in d1 and key in d2:
        d2[key] = d2[key] + d1[key]
    else:
        d2[key] = d1[key]
print(d2)