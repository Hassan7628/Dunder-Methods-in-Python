class Robots:
    def __init__(self, name, material, weight):
        self.name = name
        self.material = material
        self.weight = weight
        self.is_sitting = False

    def intro(self):
        return f"I am {self.name}, I am made up of {self.material} and I weight {self.weight}."

    def stand(self):
        self.is_sitting = False
        return f"{self.name} is currently standing"

    def sit(self):
        self.is_sitting = True
        return f"{self.name} is currently sitting"


r1 = Robots("R2D2", "Steel", "65kg")

print(r1.intro() + "\n")

print(r1.is_sitting)
print(r1.sit())
print(r1.is_sitting, "\n")