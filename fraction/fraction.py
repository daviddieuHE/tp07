from fractions import Fraction

class Fraction:
    """Class representing a fraction and operations on it

    Author : D. Dieu
    Date : Décembre 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num, den):
        """This builds a fraction based on some numerator and denominator.

        PRE :   num doit être un entier, den doit être un entier différent de 0
        POST :  inistalise la classe fraction
        RAISES :    num ou den be sobt pas des entiers -> typeError
                    den vaut 0 -> ZeroDivision Error
        """
        self.num = num
        self.den = den

        try:
            num = int(num)
            den = int(den)
            print(num/den)
        except ZeroDivisionError:
            print("vous ne pouvez pas diviser par zéro")
        except ValueError:
            print("veuillez entrer des nombres entiers")


    @property
    def numerator(self):
        return self.num

    @property
    def denominator(self):
        return self.den

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE :   la fraction du init
        POST :  une chaine de caractère représentant la fraction réduite
        """
    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE :   la fraction du init
        POST :  une chaine de caractère la forme réduite de la fraction représentée en additionnant un entier à une fraction.
        """
        pass

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE :  2 entiers ou fractions
         POST : l'addition de self et other
         RAISE : si other n'est pas un entier -> typeError
         """
        pass

    def __sub__(self, other):
        """Overloading of the - operator for fractions

         PRE :  2 entiers ou fractions
         POST : la soustraction de self et other
         RAISE : si other n'est pas un entier -> typeError
        """
        pass

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE :   other est également une fraction
        POST :  la multiplication de self et other
        RAISE : si other n'est pas une fraction contenant des entiers -> typeError
        """
        pass

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : other est également une fraction
        POST : renvoi le résultat de la division de self par other sous forme d'une nouvelle fraction
        RAISE : si other n'est pas une fraction contenant des entiers -> typeError
        """
        pass

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : other est également une fraction
        POST : la fraction élevée à la puissance other
        RAISE : si other n'est un entiers -> typeError
        """
        pass

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : other est également une fraction
        POST :  si les 2 fraction on la meme forme décimale -> renturn True
                sinon return False
        RAISE : si other n'est pas une fraction contenant des entiers -> typeError

        """

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : la fraction self
        POST : renvoi la forme décimale de la fraction
        """
        pass

    # ------------------ Properties checking ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE :   la fraction du init
        POST :  si la fraction vaut 0 -> return True
                si la fraction ne vaut pas 0 -> return False
        """
        pass

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE :   la fraction du init
        POST :  si la fraction est un entier -> return True
                si la fraction n'est pas un entier -> return False
        """
        pass

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE :   la fraction du init
        POST :  si la valeur absolue de la fraction est supérieur à 1 -> return True
                si la valeur absolue de la fraction est inférieur à 1 -> return False
        """

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE :   la fraction du init
        POST :  si le numérateur de la fraction est 1 -> return True
                si le numérateur de la fraction est différent de 1 -> return False
        """
        pass

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE :   other est également un entier représenté sous forme de fraction
        POST :  si le numérateur de la valeur absolue de la soustraction de self et other vaut 1 -> return True
                si pas -> return False
        RAISE : si other n'est pas un entier -> typeError
        """
        pass
