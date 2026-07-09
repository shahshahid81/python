class ReadOnlyValue:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        # self is the instance of ReadOnlyValue class
        # instance is the instance of the class that is using the Descriptor
        # owner is the class that is using the Descriptor

        # <__main__.ReadOnlyValue object at 0x104bc8d90> <__main__.SomeClass object at 0x104bc8bb0> <class '__main__.SomeClass'>
        print(self, instance, owner)
        return self.value

    def __set__(self, instance, value):
        raise ValueError(f"'my_value' cannot be set. Provided value: {value}")


class SomeClass:
    my_value = ReadOnlyValue(10)


some_class = SomeClass()
print(some_class.my_value)
# ValueError: 'my_value' cannot be set. Provided value: 20
# some_class.my_value = 20
