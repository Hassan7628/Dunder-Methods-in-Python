# Post stuff
a = "hello"
b = "hello"
print(a == b)


class Robot:
    def __init__(self, name, material, weight):
        self.name = name
        self.material = material
        self.weight = weight


r1 = Robot("R2D2", "Iron", 52)
r2 = Robot("R2D2", "Iron", 52)
r3 = r1

print(r1 == r2)
print(r1 == r3)


print("\n\n")


# eq method
class Drone:
    def __init__(self, id, material, weight) -> None:
        self.id = id
        self.material = material
        self.weight = weight

    def __eq__(self, other):
        if self.weight == other.weight:
            return True

        else:
            return False


d1 = Drone(1, "Alumininum", 56)
d2 = Drone(1, "Iron", 56)
d3 = d1

print(d1 == d3)

print(d1 == d2)