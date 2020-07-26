string = 'MyCamelHas3Humps'

def kebabize(string):
    clear_string = ''
    for letter in string:
        if letter.islower() == True:
            clear_string += letter
        elif letter.istitle() == True:
            clear_string += ('-' + letter.lower())
        else:
            clear_string += ''
    return clear_string.lstrip('-')

print(kebabize(string))
