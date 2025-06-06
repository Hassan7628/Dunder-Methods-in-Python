with open("file1.txt", "r") as file:
    data = file.read()
    print(data)


# using enter and exit:
class Filereader:
    def __init__(self, name, method):
        self.file = open(name, method)

    def __enter__(self):
        return self.file

    def __exit__(self, type, value, traceback):
        self.file.close()

        if type == FileNotFoundError:
            print("File not found")
            return (
                True  # tells to not raise exception because it is handeled gracefully
            )


with Filereader("file1.txt", "r") as file:
    print(file.read())

    raise FileNotFoundError