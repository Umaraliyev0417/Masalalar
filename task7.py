txt = "Hello World 12345"
def count_all(txt):
    dict = {'LETTERS': 0, 'DIGITS': 0}
    for x in txt:
        if x.isalpha():
            dict['LETTERS'] += 1
        if x.isdigit():
            dict['DIGITS'] += 1
    return dict

print(count_all(txt))