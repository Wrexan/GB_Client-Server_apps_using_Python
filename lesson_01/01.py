# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате
# и проверить тип и содержание соответствующих переменных.
# Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode и также
# проверить тип и содержимое переменных.

def check_n_print(sl):
    for s in sl:
        print(f'{s} is {type(s)}')


words_to_check = ['разработка', 'сокет', 'декоратор']
check_n_print(words_to_check)

words_to_check = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
                  '\u0441\u043e\u043a\u0435\u0442',
                  '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']
check_n_print(words_to_check)
