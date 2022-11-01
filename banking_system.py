#Parent Class

class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def show_details(self):
        print("Persnal Details")
        print("")
        print("Name", self.name)
        print("Age", self.age)
        print("Gender", self.gender)    
        
        
#Child Class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)     
        self.balance = 0
    
    def deposit(self, amount):
        self.amount = amount
        self.balance =  self.balance + amount   
        print("Amount updated: Rs", self.balance)
        
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficent", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Balence updated",self.balance)
            
    def view_balance(self):
        self.show_details()
        print("Account balance", self.balance)
        
    
        

    
sr = Bank('shri', 21,'Male')
sr.deposit(400)
sr.withdraw(30)
sr.withdraw(4)
sr.view_balance()
# print(sr.name)
# print(sr.gender)
        
# sr = User('sr', 22, 'we')
# sr1 = User('sr1', 23, 'we work')
# sr.show_details()
# sr1.show_details()