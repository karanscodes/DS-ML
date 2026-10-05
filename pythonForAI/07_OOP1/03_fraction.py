class Fraction:
    # parameterised
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    # to display/print the object
    def __str__(self):
        return f"{self.num}/{self.denom}"

    def __add__(self, other):
        new_num = self.num * other.denom + other.num * self.denom
        new_denom = self.denom * other.denom

        return f"{new_num}/{new_denom}"

    def __sub__(self,other):
        new_num = self.num * other.denom - other.num * self.denom
        new_denom = self.denom * other.denom

        return f"{new_num}/{new_denom}"
    
    def __mul__(self, other):
        new_num = self.num * other.num
        new_denom = self.denom * other.denom

        return f"{new_num}/{new_denom}"
    
    def __truediv__(self, other):
        new_num = self.num * other.denom
        new_denom = self.denom * other.num

        return f"{new_num}/{new_denom}"
    
    # custom method
    def convert_to_decimal(self):
        return self.num/self.denom

fr1 = Fraction(1,3)
fr2 = Fraction(1,3)

print(fr1)
print(fr2)
print(fr1 + fr2)
print(fr1 - fr2)
print(fr1 * fr2)
print(fr1 / fr2)
print(fr1.convert_to_decimal())