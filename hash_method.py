class Toys:
    def __init__(self, name, material, price) -> None:
        self.name = name
        self.material = material
        self.price = price

    # Hash converts the value into a integers and find the corresponding key in a dictionary one it finds it, It compares it and if it is True, return the value.

    def __eq__(self, other):
        if self.price == other.price and self.material == other.material:
            return True
        else:
            return False

    def __hash__(self) -> int:
        return hash((self.price, self.material))


t1 = Toys("doll", "plastic", 100)
t2 = Toys("car", "plastic", 100)

print(hash(t1) == hash(t2))

print(t1 == t2)