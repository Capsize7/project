from collections import namedtuple
class Aries:
    att = 'fire'
    start = [21, 3]
    end = [20, 4]
    def description(self):
        return f'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).'


class Taurus:
    att = 'earth'
    start = [21, 4]
    end = [21, 5]
    def description(self):
        return f'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).'


class Gemini:
    att = 'air'
    start = [22, 5]
    end = [21, 6]
    def description(self):
        return f'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).'

class Cancer:
    att = 'water'
    start = [22, 6]
    end = [22, 7]
    def description(self):
        return f'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).'


class Leo:
    att = 'fire'
    start = [23, 7]
    end = [21, 8]
    def description(self):
        return f'Лев - пятый знак зодиака</i>, солнце (с 23 июля по 21 августа).'

class Virgo:
    att = 'earth'
    start = [22, 8]
    end = [23, 9]
    def description(self):
        return f'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).'

class Libra:
    att = 'air'
    start = [24, 9]
    end = [23, 10]
    def description(self):
        return f'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).'

class Scorpio:
    att = 'water'
    start = [24, 10]
    end = [22, 11]
    def description(self):
        return f'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).'

class Sagittarius:
    att = 'fire'
    start = [23, 11]
    end = [22, 12]
    def description(self):
        return f'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).'

class Capricorn:
    att = 'earth'
    start = [23, 12]
    end = [20, 1]
    def description(self):
        return f'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).'


class Aquarius:
    att = 'air'
    start = [21, 1]
    end = [19, 2]
    def description(self):
        return f'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).'

class Pisces:
    att = 'water'
    start = [20, 2]
    end = [20, 3]
    def description(self):
        return f'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).'

a = Pisces
print(a.__name__)