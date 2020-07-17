<<<<<<< HEAD
s = 'Pack my box with five dozen liquor jugs'

import string

def is_pangram(s):
    return set(string.ascii_lowercase) <= set(s.lower())

print(is_pangram(s))
=======
s = 'Pack my box with five dozen liquor jugs'

import string

def is_pangram(s):
    return set(string.ascii_lowercase) <= set(s.lower())

print(is_pangram(s))
>>>>>>> c3f95e5cd5a45918ce2152d4c42e23f8194e6df1
