# When we build multiple classes for a complex project, classes talk with each other. They have a relationship with one another 

# Aggregation : "has a" relationship. One class owns the other class

# example: Customer "has a" Address, Restaurant 'has a' Menu

class Customer:
    def __init__(self, name, address, gender):
        self.name = name
        self.gender = gender
        # we'll have object address here
        self.address = address
        
    def print_address(self):
        print(self.address.get_city(), self.address.pin, self.address.state)

    def edit_profile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.address.edit_address(new_city, new_pin, new_state)

class Address:
    def __init__(self, city, pin, state):
        self.__city = city
        self.pin = pin
        self.state = state
    
    def get_city(self):
        return self.__city

    def edit_address(self, new_city, new_pin, new_state):
        self.__city = new_city
        self.pin = new_pin
        self.state = new_state

add1 = Address("bhopal", 462003, 'madhyapradesh')
c = Customer("Karan", add1, "man")

c.print_address()
c.edit_profile('twin', 'tokyo', 696969, 'to')

c.print_address()