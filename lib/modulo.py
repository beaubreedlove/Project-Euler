
class Modulo:

    mod = None

    known_powers = {}
    known_products = {}

    def __init__(self, mod):
        self.mod = mod

    def power(self, a, b):
        a = a % self.mod
        # b = b % (self.mod - 1)

        if a == 0:
            return 0
        if a == 1:
            return 1
        if b == 0:
            return 1

        return self._power(a, b)

    def _power(self, a, b):
        # test rearranging these
        triplet = (a, b, self.mod)

        if triplet in Modulo.known_powers:
            return Modulo.known_powers[triplet]
        if b == 1:
            return a

        # if random.random() < .1:
        #     return False

        c = b/2
        d = self._power(a, c)
        e = self._power(a, b-c)

        f = self.multiply(d, e)
        Modulo.known_powers[triplet] = f
        return f

    def multiply(self, a, b):
        a = a % self.mod
        b = b % self.mod

        if b < a:
            tmp = a
            a = b
            b = tmp

        if a == 0:
            return 0

        return self._multiply(a, b)

    # Calculates a*b % self.mod assuming 1 < a <= b < self.mod
    def _multiply(self, a, b):
        triplet = (a, b, self.mod)

        if triplet in self.known_products:
            return Modulo.known_products[triplet]
        if a == 1:
            return b

        c = a/2
        d = self._multiply(c, b)
        e = self._multiply(a-c, b)

        f = (d + e) % self.mod
        Modulo.known_products[triplet] = f
        return f
