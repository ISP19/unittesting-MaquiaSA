import math

class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """
    
    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        if numerator == 0 and denominator == 0:
            raise ValueError
        elif not isinstance(numerator, int):
            raise TypeError
        elif not isinstance(denominator, int):
            raise TypeError
        else:
            gcd = math.gcd(numerator,denominator)
            if denominator < 0:
                numerator *= -1
                denominator *= -1
            self.numerator = int(numerator/gcd)
            self.denominator = int(denominator/gcd)
        # except:
        #     self.numerator = numerator
        #     self.denominator = denominator


    def __str__(self):
        if self.denominator == 1 or self.numerator == 0:
            return '{0}'.format(int(self.numerator/self.denominator))
        return '{0}/{1}'.format(self.numerator, self.denominator)

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        new_numerator = self.numerator * frac.denominator + frac.numerator * self.denominator
        new_denominator = self.denominator * frac.denominator
        if new_numerator == 0 and new_denominator == 0:
            raise ValueError
        return Fraction(new_numerator, new_denominator)
    
    def __sub__(self, frac):
        """Return the difference of two fractions as a new fraction."""
        new_numerator = self.numerator * frac.denominator - frac.numerator * self.denominator
        new_denominator = self.denominator * frac.denominator
        return Fraction(new_numerator, new_denominator)
    
    def __mul__(self, frac):
        """Return the multipication of two fractions as a new fraction."""
        new_numerator = self.numerator * frac.numerator
        new_denominator = self.denominator * frac.denominator
        return Fraction(new_numerator, new_denominator)


    #TODO write __mul__ and __str__.  Verify __eq__ works with your code.
    #Optional have fun and overload other operators such as 
    # __sub__ for f-g
    # __gt__  for f > g
    # __neg__ for -f (negation)

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        return self.numerator == frac.numerator and self.denominator == frac.denominator

