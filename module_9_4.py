from random import choice

# Задача с Lambda-функцией:
first = 'Мама мыла раму'
second = 'Рамена мало было'

print(list(map(lambda x, y: x == y, first, second)))


# Задача на замыкание:
def get_advanced_writer(file_name):

    def write_everything(*data_set):
        with open(file_name, 'a') as file:
            for data in data_set:
                file.write(str(data) + '\n')
    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


# Задача с методом __call__:
class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self, *args):
        return choice(self.words)


ball = MysticBall('Да', 'Нет', 'Наверно', 'Возможно', 'Вероятно', 'Вполне себе', 'Скорее всего', 'Определенно',
                  'Точно так', 'Без вариантов', '100%!')
for _ in range(20):
    line = ball()
    print(line if line != '100%!' else f'{line} - Так и надо отвечать!')
