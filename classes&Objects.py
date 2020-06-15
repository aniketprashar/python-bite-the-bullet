import random


class Rupee_coins:  # starts with uppercase. Classes are base templates
    value = "1.00"
    color = "Silver"
    heads = True  # these are states of a class


coin1 = Rupee_coins()  # object
print(type(coin1))  # <class '__main__.Rupee_coins'>

print(coin1.color)  # Silver

coin1.color = "greenish"
print(coin1.color)  # greenish

# -------------------------------------------------------------------------------------------------------------------------------------------------- #
#                                                            Constructors And Destructors                                                            #
# -------------------------------------------------------------------------------------------------------------------------------------------------- #


class Rupee:
    def __init__(self, rare_coin=False):  # constructors with self as parameter. It doesn't need to be self. It is just a convention. It doesn't return anything
        self.color = "Silver"
        self.heads = True
        self.rare_coin = rare_coin  # without this if else cannot be used
        if self.rare_coin:
            self.value = 1.25
        else:
            self.value = 1.00


coin1 = Rupee(rare_coin=True)
coin2 = Rupee()
print(coin1.rare_coin)  # True
print(coin2.rare_coin)  # False

# --------------------------------------------------------------------- Methods -------------------------------------------------------------------- #


class Rupee:
    def __init__(self, rare_coin=False):  # constructors with self as parameter. It doesn't need to be self. It is just a convention. It doesn't return anything
        self.color = "Silver"
        self.heads = True
        self.rare_coin = rare_coin  # without this if else cannot be used
        if self.rare_coin:
            self.value = 1.25
        else:
            self.value = 1.00

    def rusted_coin(self):  # self is mandatory
        self.color = "greenish"


coin1 = Rupee()
coin1.rusted_coin()
print(coin1.color)  # greenish

# ------------------------------------------------------------------- Destructors ------------------------------------------------------------------ #


class Rupee:
    def __init__(self, rare_coin=False):  # constructors with self as parameter. It doesn't need to be self. It is just a convention. It doesn't return anything
        self.color = "Silver"
        self.heads = True
        self.rare_coin = rare_coin  # without this if else cannot be used
        if self.rare_coin:
            self.value = 1.25
        else:
            self.value = 1.00

    def __del__(self):
        print("coin spent!")


coin1 = Rupee()
print(coin1)
# <__main__.Rupee object at 0x7fd50e99af40>
# coin spent!
del coin1
print(coin1)  # NameError: name 'coin1' is not defined

# -------------------------------------------------------------------------------------------------------------------------------------------------- #
#                                                                   Abstract Class                                                                   #
# -------------------------------------------------------------------------------------------------------------------------------------------------- #


class Coin:
    def __init__(self, rare=False, clean=True, heads=True):
        self.israre = rare
        self.isclean = clean
        self.heads = heads
        if self.israre:
            self.value = self.original_value*1.25
        else:
            self.value = self.original_value

        if self.isclean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color

    def rust(self):
        self.color = self.rusty_color

    def clean(self):
        self.color = self.clean_color

    def __del__(self):
        print("coin spent")


class Rupee(Coin):  # Rupee is inheriting from its parent class Coin
    def __init__(self):
        data = {
            "original_value": 1.00
            "clean_color"":"gold"
            "rusty_color": "greenish"

        }
