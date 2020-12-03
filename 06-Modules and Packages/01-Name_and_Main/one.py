def func():
    print("func() ran in one.py")

print("top-level print inside of one.py")

if __name__ == "__main__":
    print("one.py is being run directly")
else:
    print("one.py is being imported into another module")

# usually dont have the else but the first part is the run the scripts
# define functions and classes at the top and then use the if __name__ part to
# execute the logic of the script
