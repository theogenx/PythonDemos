# https://dzone.com/articles/python-exception-handling-try-except-and-finally-i

# Python program to demonstrate the example of raising Exception

# try block

try: 

    # raising a named exception

    raise NameError("Hello!!") 

# except block which will catch the raised NameError 

except NameError:

    print ("An exception")

    # again raising an exception and this will not be handled by the catch block

    raise 