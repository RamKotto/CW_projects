a = 21
b = 49

def euclidean(a, b):
    while a % b != 0:
        if a > b:
            a -= b
        elif a < b:
            b -= a
    return b

print(euclidean(a, b))
