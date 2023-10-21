# Method Overloading
from multipledispatch import dispatch


@dispatch(int, int)
def sum_of_two_num(a, b):
    print("This is Integer")
    print(a + b)


@dispatch(int, float)
def sum(a, b):
    print("This is float")
    print(a + b)


@dispatch(int, int, int)
def sum(a, b, c):
    print(a + b + c)


sum(1, 2)

# Operator Overloading
c = 1 + 2
d = "hel" + "lo"
print(c)
print(d)


def sum(a=None, b=None, c=None):
    if c is None:
        print(a + b)
    elif b is None:
        print(a + c)
    elif a is None:
        print(b + c)
    else:
        print(a + b + c)


sum(1, 2, 3)


def do_something(param1: str, param2: list, param3: int = None):
    pass


# Method_Overriding
class Globe:

    @staticmethod
    def capital(self):
        print("Globe does not have capital")


class India(Globe):

    def capital(self):
        print("The capital is Delhi")


class US(Globe):

    def capital(self):
        print("The capital is WDC")


my_object = US()
my_object.capital()

a = 1
b = 0
c = None
try:
    c = a / b
except ZeroDivisionError as ex:
    print(f"my exception is: {ex}")
except Exception:
    print("This is parent exception")
# except TypeError:
#     print("I got  exception for type error but let me proceed")
# except:
#     print("I got some exception i dont know")
finally:
    print("Finally block")
print(c)

d = 1
e = 4
f = d * e
print(f)
