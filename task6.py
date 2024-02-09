lst = ["a", "b", "c"]

def mapping(lst):
    dict = {}
    for x in lst:
        dict[x] = x.upper()
    return dict

print(mapping(lst))