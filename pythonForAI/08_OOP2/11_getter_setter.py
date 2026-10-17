# if i really want to change my private variables in python, i'd use getter and setter methods
# getter : private ka value bahar dikhana
# setter : private ka value bahar se change karna

class Atm:
    def __init__(self):
        self._pin = ''
        self._balance = 0
    
    def get_balance(self):
        return (self._balance)

    def set_balance(self, val):
        if type(val) == int:
            self._balance = val
        else:
            print("Beta Bahut Pitega")
    
obj = Atm()
print(obj.get_balance())
obj.set_balance(1000)

print(obj.get_balance())
