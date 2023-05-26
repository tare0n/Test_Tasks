import re

# Task №1

# refactor incorrect functions:

# 1. def to_camel_case(text):
#    return re.split('_|-', text)[1] + ''.join(word.title() for word in re.split('_|-', "text")[1::])


def to_camel_case(text):
    return re.sub(r"(_|-)+", " ", text).title().replace(" ", "")


# 2. class SingletonMeta(type):
#
#       _instances = {}

#       def *str*(cls, *args, **kwargs):
#           if cls in cls._instances:
#               instance = super().*call*(*args, **kwargs)
#               cls._instances[cls] = instance
#       return cls._instances[cls]


class SingletonMeta(type):

    def __init__(self):
        self._instances = {}

    def str(cls, *args, **kwargs):
        if cls in cls._instances:
            instance = super().call(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

#    3. count_bits = lambda: bin(n).count('1')


count_bits = lambda n: bin(n).count('1')

#   4. def digital_root(n):
#     return if n < 10 n else digital_root(summ(map(int,str(n))))


def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int, str(n))))


#  5. even_or_odd = lambda number: "Even" if % 2 == 0 else "Odd"

even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"

