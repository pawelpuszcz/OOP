# implement function named 'stick' which takes any quantity of arguments and
# returns object type 'str' which joins all the arguments type 'str' given to 
# the function separated by '#'


def stick(*args):
    strings = []
    for arg in args:
        if type(arg) == str:
            strings.append(arg) 
    return '#'.join(strings)

print(stick('sport', 'summer'))
print(stick(3,5,7))
print(stick(False, 'time', True, 'workout', [], 'gym'))