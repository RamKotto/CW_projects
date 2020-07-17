<<<<<<< HEAD
s = 'Pack my box with five dozen liquor jugs'

def is_pangram(s):
    s = s.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    for i in alphabet:
        if i in s:
            count += 1
    if count == 26:
        return True
    else:
        return False


print(is_pangram(s))
=======
s = 'Pack my box with five dozen liquor jugs'

def is_pangram(s):
    s = s.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    for i in alphabet:
        if i in s:
            count += 1
    if count == 26:
        return True
    else:
        return False


print(is_pangram(s))
>>>>>>> c3f95e5cd5a45918ce2152d4c42e23f8194e6df1
