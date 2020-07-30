#           Examples:
# "10 ohms"        "brown black black gold"
# "100 ohms"       "brown black brown gold"
# "220 ohms"       "red red brown gold"
# "330 ohms"       "orange orange brown gold"
# "470 ohms"       "yellow violet brown gold"
# "680 ohms"       "blue gray brown gold"
# "1k ohms"        "brown black red gold"
# "4.7k ohms"       "yellow violet red gold"
# "10k ohms"       "brown black orange gold"
# "22k ohms"       "red red orange gold"
# "47k ohms"       "yellow violet orange gold"
# "100k ohms"      "brown black yellow gold"
# "330k ohms"      "orange orange yellow gold"
# "2M ohms"        "red black green gold"


ohms_string = "47k ohms"


def encode_resistor_colors(ohms_string):
    color_digit = {'0': 'black',
                   '1': 'brown',
                   '2': 'red',
                   '3': 'orange',
                   '4': 'yellow',
                   '5': 'green',
                   '6': 'blue',
                   '7': 'violet',
                   '8': 'gray',
                   '9': 'white'}
    multiplier = {'1': 'black',
                  '2': 'black',
                  '3': 'brown',
                  '4': 'red',
                  '5': 'orange',
                  '6': 'yellow',
                  '7': 'green',
                  '8': 'blue',
                  '9': 'violet',
                  '10': 'grey',
                  '11': 'white'}

    number = ohms_string.rstrip('ohms')
    snumber = ''
    mult = ''
    answer = ''
    fnum = ''
    check = []
    a, b, c = '', '', ''

    # First and Second colors:

    for i in number:
        if i.isdigit() == True:
            snumber += i
    if len(snumber) > 1:
        a = snumber[0]
        b = snumber[1]
        answer = str(color_digit.get(a)) + ' ' + str(color_digit.get(b))
    elif len(snumber) == 1:
        a = snumber[0]
        answer = str(color_digit.get(a)) + ' ' + 'black'

    # Multiplier color:

    for s in number:
        if s.isdigit() == True or s == '.':
            fnum += s

    for j in number:
        check.append(j)
        if 'M' in check:
            mult = 1000000
        elif 'k' in check:
            mult = 1000
        else:
            mult = 1

    c = str(int(eval(str(fnum) + '*' + str(mult))))

    return answer + ' ' + (multiplier.get(str(len(c)))) + ' gold'



print(encode_resistor_colors(ohms_string))