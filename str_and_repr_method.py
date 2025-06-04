class Human():
    def __init__(self,name,age,persoanlity):
        self.name=name
        self.age=age
        self.personality=persoanlity

    def __str__(self):
        return f"name: {self.name}, age: {self.age}, personality: {self.personality}" # For easier readability
    
    def __repr__(self):
       return (f"Human({self.name}, {self.age}, {self.personality})") # For debugging
    
h1=Human("Ali", 18, "calm")
print(h1)