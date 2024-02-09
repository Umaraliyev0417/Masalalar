lst = [
  {"name": "John", "age": 21, "budget": 23000},
  {"name": "Steve",  "age": 32, "budget": 40000},
  {"name": "Martin",  "age": 16, "budget": 2700}
    ]
def get_budgets(lst):
    result = 0
    for x in lst:
        result += x['budget']
    return result

print(get_budgets(lst))