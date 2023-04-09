import random



""" def find():
    list = [1,2,3,4,5,6,7,8,9,10]
    guess = random.choice(list)
    user_guess = input('Guess a number between 1 and 10')
#    while user_guess == guess:
#        print('Correct')
        
    while user_guess == guess:
        print('correct')
    if user_guess != guess:
        for x in range(15):
            user_guess = input('Try again')
    print(guess) """

    
   





class Employee:
    raise_amount = 2
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    def fullname(self):
        return self.first + '.' + self.last
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
class Developer(Employee):
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang
class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        self.employees = []
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emps(self):
        for emp in self.employees:
            print(emp.fullname())

Ethan = Employee('Ethan', 'DeJesus',50000)
Future = Developer('Ethan', 'De Jesus', 50000,'Python')
the_manager = Manager('Boss','Ok',100000,[])
the_manager.add_emp(Ethan)
the_manager.print_emps()