###A class that computes a specific power of other numbers
class Power(object):

        default_exponent = 2

        def __init__(self, exponent = default_exponent):
            self.exponent = exponent

        def of(self, x):
            return x ** self.exponent
#subclass for power of real numbers
class RealPower(Power):

    def ofNumber(self, x):
        if isinstance(self.exponent, int) or x >= 0:
            return x ** self.exponent
        raise ValueError(
            'Fractional powers of negative numbers are imaginary')
    print('Power:', Power)
    print('Power.default_exponent', Power.default_exponent)

    square = Power()
    root = Power(0.5)
    print('square of(3)', square.ofNumber(3))