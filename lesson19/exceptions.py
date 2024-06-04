class theError(Exception):
    pass

x = 2
try:
    raise theError("This is an error.")
    #print(x / 1)
    # raise Exception("Exception error.")
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed.")
    #     raise Exception("error")
except NameError:
    print('NameError means something is probably undefined.')
except ZeroDivisionError:
    print('Error: divided by zero.')
except Exception as error:
    print(f"Warning: {error}")
else:
    print('There is no errors.')
    print(f"The result of x is {x}.")
finally:
    print("I am going to print with or without an error.")