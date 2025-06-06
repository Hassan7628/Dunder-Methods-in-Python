# iter and next are used to make an object iterable:

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


print("\n\n")
# understanding iter and next:
int = [1, 2, 3, 4, 5]  # iterable
it = iter(int)  # iterator

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


print("\n\n")


# In class:
class Students:
    def __init__(self, name):
        self.name = name
        self.index = 0

    def __iter__(self):  # iter returns the iterator
        return self  # the object itself is the iterator

    def __next__(self):
        if self.index >= len(self.name):
            raise StopIteration

        else:
            result = self.name[self.index]
            self.index += 1
            return result


stds = ["ali", "ahmed", "kinza"]
students = Students(stds)

for std in students:
    print(std)