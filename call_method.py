# func() is same as func.__call__()


class Greet:
    def __init__(self, name):
        self.name = name
        print(f"hello {name}")

    def again(self):
        print(f"{self.name} says hi again!")

    def __call__(self):
        print("Who summoned me!")


g1 = Greet("hassan")
g1.again()
g1()


print("\n\n")


class Add:
    def __init__(self, base) -> None:
        self.base = base

    def __call__(self, value):
        self.base += value


val1 = Add(5)
val1(22)
print(val1.base)
val1(6)
print(val1.base)