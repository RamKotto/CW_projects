a = "abcdeFg"
b = "defgG"

def work_on_strings(a, b):
    corA = [letter if b.lower().count(letter.lower()) % 2 == 0 else letter.swapcase() for letter in a]
    corB = [letter if a.lower().count(letter.lower()) % 2 == 0 else letter.swapcase() for letter in b]
    return ''.join(corA) + ''.join(corB)

print(work_on_strings(a, b))


