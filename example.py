class Robot:
    num = 1

    def __init__(self, name, material, weight):
        self.name = name
        self.material = material
        self.weight = weight
        self.id = {}
        self.current_id = 1
        self.assign_id()

    def __str__(self):
        return f"My name is {self.name}, I am made up of {self.material} and I weight {self.weight}kg"

    def __repr__(self):
        return f"Robot({self.name}, {self.material}, {self.weight}kg)"

    def generate_id(self):
        id_to_return = self.__class__.num
        self.__class__.num += 1  # appends one so next id is +1.
        return id_to_return

    def assign_id(self):
        new_id = self.generate_id()
        self.id[self.name] = new_id
        self.current_id = new_id

    def __setitem__(self, key, value):
        self.id[key] = value

    def __getitem__(self, item):
        return self.id[item]

    def __eq__(self, other):
        if self.weight == other.weight and self.name == other.name:
            return True

        return False

    def __hash__(self):
        return hash((self.weight, self.name))


r1 = Robot("r2d2", "iron", 56)
r2 = Robot("blop", "iron", 56)

# r1["r2d2"]=5
print(r1.id)
print(r2.id)

print(r1["r2d2"])

print(r1 == r2)
print(hash(r1) == hash(r2))


print("\n\n")


class Students:
    def __init__(self, name):
        self.name = name
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.name):
            raise StopIteration

        else:
            result = self.name[self.index]
            self.index += 1
            return result


stds = ["ali", "ahmed", "hassan"]
students = Students(stds)

for i in students:
    print(i)


class FileReader:
    def __init__(self, name, method):
        self.file = open(name, method)

    def __enter__(self):
        return self.file

    def __exit__(self, type, value, traceback):
        self.file.close()

        if type == FileNotFoundError:
            print("\nfile not found!")
            return True

        return False


with FileReader("example.txt", "r") as file:
    read = file.read()

    raise FileNotFoundError