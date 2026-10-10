# parent
class User: 
    def __init__(self):
        self.name = "Karan"
        self.rollno = 100

    def login(self):
        print('login')
    
# child
class Student(User):

    
    def enroll(self):
        print("enroll into the course")
    
u = User()
s = Student()
print(s.name, s.rollno)
s.login()
s.enroll()