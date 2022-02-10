class Lemonade:

    def __init__(self, add_tasty='Обычная газировка'):
        self.add_tasty = add_tasty

    def drink_info(self):

        if self.add_tasty != 'Обычная газировка' and self.add_tasty != '':
            return f'Газировка и {self.add_tasty}'

        else:
            return 'Обычная газировка'


lemonade = Lemonade('клубника')

print(lemonade.drink_info())