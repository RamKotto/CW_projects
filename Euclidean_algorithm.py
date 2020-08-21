a = 21
b = 49

def euclidean(a, b):
    while a % b != 0:
        if a > b:
            a -= b
        elif a < b:
            b -= a
    if a % b == 0:
        return b
    else:
        return a

print(euclidean(a, b))
