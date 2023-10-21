# OOP concepts - Object Oriented Programming

# Object- is an instance of class
# Class- is blueprint or template

class Car:

    def __init__(self, engine, tyre):  # parametrized constructor
        self.engine_type = engine
        self.tyre_type = tyre

    def engine(self):
        print(f"This is {self.engine_type} engine")

    def tyre(self):
        print(f"This is {self.tyre_type} tyre")

    @classmethod
    def this_is_class_method(cls):
        print("This is exclusive class method")


first_object = Car("First car", "First car")
first_object.engine()
first_object.tyre()
first_object.this_is_class_method()
second_object = Car("Second car", "Second car")
second_object.engine()
second_object.tyre()
second_object.this_is_class_method()
# first_object.engine()
# first_object.tyres()
# # print(first_object.car_class_variable)
# first_object.this_is_class_method()
