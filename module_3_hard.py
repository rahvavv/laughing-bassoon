data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*args):
    count = 0
    for i in args:
        if isinstance(i, int):
            count += i
        elif isinstance(i, str) and len(i) > 0:
            count += len(i)
        elif isinstance(i, (list, tuple, set)):
            count += calculate_structure_sum(*i)
        elif isinstance(i, dict):
            count += calculate_structure_sum(*i.keys())
            count += calculate_structure_sum(*i.values())
    return count


result = calculate_structure_sum(data_structure)
print(result)
