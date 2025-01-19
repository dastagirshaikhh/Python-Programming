list1 = [{'A': 2, 'B': 8, 'C': 10},
         {'D': 1, 'E': 10, 'F': 9},
         {'G': 3, 'H': 4}]

print("original list : " + str(list1))

res = [sub for sub in list1 if sorted(
    list(sub.values())) == list(sub.values())]

print("filtered Dictionaries : " + str(res))
