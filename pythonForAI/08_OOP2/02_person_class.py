class Person:

    def __init__(self, name, country):
        self.name = name
        self.country = country
    
    def greet(self):
        if self.country == 'india':
            print(f"Namaste {self.name}!")
        else:
            print(f"Hello {self.name}!")
    
guy = Person("Karan", "india")
girl = Person("Girl", 'japan')

guy.greet()
girl.greet()