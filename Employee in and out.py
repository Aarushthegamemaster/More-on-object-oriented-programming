class Employee:

    def __init__(self):
        print("Employee has been created")
    def __del__(self):
        print("The Destructor has been called")
def Create_obj():
    print("Making Object")
    obj = Employee()
    print("Function and...")
    return obj

print('Calling Create_obj() function')
obj = Create_obj()
print("Program end")