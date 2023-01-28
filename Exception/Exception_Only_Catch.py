# https://dzone.com/articles/python-exception-handling-try-except-and-finally-i

# declaring a variable with the integer value

a=5

# declaring another variable with the integer value

b=0

try:

    # trying to divide both values

    print (a/b)

    # exception will occur as we are trying to divide a 

    # number by zero

# except block to handle TypeError exception

except TypeError:

    print('Operation is not supported')

# except block to handle ZeroDivisionError exception

except ZeroDivisionError:

    print ('Divide a number by zero is not allowed')
