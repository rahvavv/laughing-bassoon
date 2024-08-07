calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains(string, list_to_search):
    count_calls()
    return (string.lower() in [x.lower() for x in list_to_search])


print(string_info('uRbAn'))
print(string_info('pycharm'))
print(is_contains('Urban', ['urian', 'URBAN', 'uran']))
print(is_contains('Python', ['putho', 'PHOTon', 'py']))
print(calls)
