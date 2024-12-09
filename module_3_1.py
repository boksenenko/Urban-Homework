calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    print(len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    lowered_string = string.lower()
    lowered_list = [item.lower() for item in list_to_search]
    if lowered_string in lowered_list:
        return True
    else:
        return  False

string_info('bogdan')
string_info('Abrakadabra')
print(is_contains('pupa', ['Buba', 'lupa']))
print(is_contains('pupa', ['Pupa', 'lupa']))
print(calls)