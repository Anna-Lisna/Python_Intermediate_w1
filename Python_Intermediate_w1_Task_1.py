def get_common_den(number_1, number_2):
    if number_1 <= number_2:
        first = number_2
        second = number_1
    else:
        first = number_1
        second = number_2

    next_number = first % second

    while next_number != 0:
        first = second
        second = next_number
        next_number = first % second

    first_multiplier = int(number_2 / second)
    second_multiplier = int(number_1 / second)
    den = first_multiplier * second_multiplier * second

    return first_multiplier, second_multiplier, den


class MixinOperation:
    @staticmethod
    def sub(fraction_1, fraction_2):
        if fraction_1.den == fraction_2.den:
            num = fraction_1.num - fraction_2.num
            den = fraction_1.den
        else:
            first_multiplier, second_multiplier, den = get_common_den(fraction_1.den, fraction_2.den)
            num = (fraction_1.num * first_multiplier) - (fraction_2.num * second_multiplier)
        return f'{num}/{den}'

    @staticmethod
    def add(fraction_1, fraction_2):
        if fraction_1.den == fraction_2.den:
            num = fraction_1.num - fraction_2.num
            den = fraction_1.den
        else:
            first_multiplier, second_multiplier, den = get_common_den(fraction_1.den, fraction_2.den)
            num = (fraction_1.num * first_multiplier) + (fraction_2.num * second_multiplier)
        return f'{num}/{den}'

    @staticmethod
    def mul(fraction_1, fraction_2):
        num = fraction_1.num * fraction_2.num
        den = fraction_1.den * fraction_2.den
        return f'{num}/{den}'

    @staticmethod
    def truediv(fraction_1, fraction_2):
        num = fraction_1.num * fraction_2.den
        den = fraction_1.den * fraction_2.num
        return f'{num}/{den}'


class Fraction(MixinOperation):
    def __init__(self, num, den):
        self.__num = num
        self.__den = den

    @property
    def num(self):
        return self.__num

    @property
    def den(self):
        return self.__den

    @num.setter
    def num(self, num):
        self.__num = num

    @den.setter
    def den(self, den):
        if den != 0:
            self.__den = den
        else:
            print('denominator can\'t be 0')

    def __sub__(self, fraction):
        if self.den == fraction.den:
            num = self.num - fraction.num
            den = self.den
        else:
            first_multiplier, second_multiplier, den = get_common_den(self.den, fraction.den)
            num = (self.num * first_multiplier) - (fraction.num * second_multiplier)
        return self.__class__(num, den)

    def __add__(self, fraction):
        if self.den == fraction.den:
            num = self.num + fraction.num
            den = self.den
        else:
            first_multiplier, second_multiplier, den = get_common_den(self.den, fraction.den)
            num = (self.num * first_multiplier) + (fraction.num * second_multiplier)
        return self.__class__(num, den)

    def __mul__(self, fraction):
        num = self.num * fraction.num
        den = self.den * fraction.den
        return self.__class__(num, den)

    def __truediv__(self, fraction):
        num = self.num * fraction.den
        den = self.den * fraction.num
        return self.__class__(num, den)

    @classmethod
    def from_string(cls, str_value):
        value = [int(i) for i in str_value.split('/')]
        return cls(*value)

    def __str__(self):
        return '{0.num}/{0.den}'.format(self)


fraction_1 = Fraction(3, 5)
fraction_2 = Fraction(1, 7)

fraction_add = fraction_1 + fraction_2
fraction_sub = fraction_1 - fraction_2
fraction_mul = fraction_1 * fraction_2
fraction_truediv = fraction_1 / fraction_2

fraction_mixin_add = Fraction.add(fraction_1, fraction_2)
fraction_mixin_sub = Fraction.sub(fraction_1, fraction_2)
fraction_mixin_mul = Fraction.mul(fraction_1, fraction_2)
fraction_mixin_truediv = Fraction.truediv(fraction_1, fraction_2)
fraction_str = Fraction.from_string('2/5')
print(fraction_add)
print(fraction_sub)
print(fraction_mul)
print(fraction_truediv)

print(fraction_mixin_add)
print(fraction_mixin_sub)
print(fraction_mixin_mul)
print(fraction_mixin_truediv)

print(fraction_str)

