# заменяет введенное слово символами '*':
password = input('Введите пароль: ')
secret_password =  '{0:*^{1}}'.format('', int(len(password)))
print(secret_password)

# обрамляет слово символам
word = input('Какое слово будем заключать в символы: ')
how_many = int(input('Сколько символов нужно по краям: '))
symbol = input('В какие символыб бро: ')

def word_in_symbols(word, how_many, symbol):
    qty = len(word) + (how_many * 2)
    result = '{0:{1}^{2}}'.format(word, symbol, qty)
    return result

print(word_in_symbols(word, how_many, symbol))


