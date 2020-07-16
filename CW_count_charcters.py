string = 'eabaafffffff'

def count(string):
    dic = {}
    for i in string:
        dic[i] = string.count(i)

    return dic

print(count(string))

