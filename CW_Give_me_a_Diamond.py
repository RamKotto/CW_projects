n = 7

def diamond(n):

    if n < 1 or not n % 2:
        return None
    diamond = ''
    for i in range(n):
        ast = '*'*(i*2 + 1) if i <= n/2 else '*'*((n-i)*2 - 1)
        diamond += ' '*int((n-len(ast)) / 2) + ast + '\n'
    return diamond

print(diamond(n))
