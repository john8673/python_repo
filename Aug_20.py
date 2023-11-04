class Parent:

    def __init__(self):
        print("This is parent constructor")
    #
    # def _house(self):
    #     return "This is parents house"
    #
    #
    # def _vehicle(self):
    #     return "This is parents vehicle"
    #
    # def __atm_card(self):
    #     return "This is parents atm card"
    #
    # def know_number_of_accounts(self):
    #     return self.__number_of_accounts


class Child(Parent):

    def __init__(self):
        super().__init__()
        print("This is Child constructor")


class GrandChild(Child):

    def __init__(self):
        super().__init__()
        print("This is GrandChild constructor")


object1 = Child()
object2 = Parent()
x = issubclass(GrandChild, Parent)
print(x)

# object1 = Child()
# object1._house()
# object1._vehicle()
# object2 = Parent()
# object2._house()
# object2._vehicle()
# object3 = GrandChild()
# object3._house()
