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
            self.numerator = 0
            self.denominator = 0
        elif isinstance(numerator, bool):
            raise TypeError("Numerator must be integer.")
        elif not isinstance(numerator, int):
            raise TypeError("Numerator must be integer.")
        elif isinstance(denominator, bool):
            raise TypeError("Denominator must be integer.")
        elif not isinstance(denominator, int):
            raise TypeError("Denominator must be integer.")
        else:
            gcd = math.gcd(numerator,denominator)
            if denominator < 0:
                numerator *= -1
                denominator *= -1
            self.numerator = int(numerator/gcd)
            self.denominator = int(denominator/gcd)


    def __str__(self):
        """Return the string in form "a/b" when a is numerator and b is denominator.
        (or "a" when a equals to 0 or "b" equals to 1)
        """
        if self.numerator == 0 and self.denominator == 0:
            return '{0}/{1}'.format(self.numerator, self.denominator)
        if self.denominator == 1 or self.numerator == 0:
            return '{0}'.format(int(self.numerator/self.denominator))
        return '{0}/{1}'.format(self.numerator, self.denominator)

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        new_numerator = self.numerator * frac.denominator + frac.numerator * self.denominator
        new_denominator = self.denominator * frac.denominator
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
    
    def __gt__(self, frac):
        """Return True if one fraction is greater than the other. 
           (a/b > c/d if ad > bc, b and d != 0)
        """
        return self.numerator * frac.denominator > frac.numerator * self.denominator
    
    def __neg__(self):
        """Return negative form fraction of itself."""
        return self * Fraction(-1)

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        return self.numerator == frac.numerator and self.denominator == frac.denominator
