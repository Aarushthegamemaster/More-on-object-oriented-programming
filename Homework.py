class Circle:
    def area(self):
        self = int(input("What is the radius of the circle: "))
        self = (self^2) * 3.14
        print("The area of the circle is",self)
    def circumfrence(self):
        self = int(input("What is the diameter of the circle: "))
        self = self * 3.14
        print("The circumfrence of the circle is",self)

cla = Circle()
print(cla.area())
print(cla.circumfrence())