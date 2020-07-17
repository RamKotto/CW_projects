s = 'Pack my box with five dozen liquor jugs'

import string

def is_pangram(s):
    return set(string.ascii_lowercase) <= set(s.lower())

print(is_pangram(s))
