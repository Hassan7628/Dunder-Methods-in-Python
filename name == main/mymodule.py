def welcome():
    print("Welcome to my module")


print(__name__)

"""
"__name__" is the name of the file you run it in and it prints as "__main__" if 
you run it in the file but running the "__name__" of another file in another file
will give the name of the file, from where "__name__" is running.
"""

if __name__ == "__main__":  # Restrict the code under it from importing to other file
    welcome()