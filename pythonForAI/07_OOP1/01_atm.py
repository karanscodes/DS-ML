class Atm:  

    # Constructor -> special function -> superpower ->  executes itself when obj instantiated

    def __init__(self):
        self.pin = ''
        self.balance = 0

        # check for execution of __init__
        self.menu()
    
    def menu(self):
        user_input = input("""
            Hi how can I help you?
            1. Press 1 to create pin
            2. Press 2 to change pin
            3. Press 3 to check balance
            4. Press 4 to withdraw
            5. Anything else to exit
        """)  

        if user_input == '1':
            # create pin
            if self.pin != '':
                print("PIN already exists!")
                self.menu()
            else:
                self.create_pin()

        elif user_input == '2':
            # change pin
            self.change_pin()

        elif user_input == '3':
            # check balance
            self.check_balance()

        elif user_input == '4':
            # withdraw
            self.withdraw()
        else:
            exit()
    
    def create_pin(self):
        user_pin = input("Enter Your Pin: ")
        self.pin = user_pin

        user_balance = int(input("Enter Balance: "))
        self.balance = user_balance

        print("PIN created successfully!")
        self.menu()
    
    def change_pin(self):
        old_pin = input("Enter your old PIN: ")
        if old_pin == self.pin:
            # let them change the pin
            new_pin = input("Enter new pin: ")
            self.pin = new_pin

            print("PIN changed successfully!")
        else:
            print("incorrect existing pin.")
        self.menu()
    
    def check_balance(self):
        user_pin = input("Enter Your PIN: ")
        if user_pin == self.pin:
            print("Your Balance is :", self.balance)
        else:
            print("Incorrect PIN.")
        self.menu()
    
    def withdraw(self):
        user_pin = input("Enter your PIN: ")
        if user_pin == self.pin:
            # allow to withdraw
            amt = int(input("Enter the amount: "))
            if amt <= self.balance:
                self.balance = self.balance - amt
                print("Withdrawal Successful. Current Balance :", self.balance)
            else:
                print("Insufficient Funds.")

        else: 
            print("Incorrect PIN.")
        self.menu()

# object instantiation
obj = Atm()

# print(type(obj))

