class Employee:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        # note that age should be treated as private
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        MIN_AGE = 18
        MAX_AGE = 65
        if isinstance(new_age, int) and new_age >= MIN_AGE and new_age <= MAX_AGE:
            self._age = new_age
            return
        print(
            f"WARNING: {new_age} not between {MIN_AGE} and {MAX_AGE}, age not updated."
        )

    @age.deleter
    def age(self):
        # This can be done too, for demo, setting it to None
        # del self._age
        self._age = None

    @property
    def email(self):
        return f"{self.fname}.{self.lname}@email.com"

    @property
    def full_name(self):
        return f"{self.fname} {self.lname}"


john = Employee("John", "Smith", 40)
john.age = 50
print(john.email)
john.lname = "Jones"
print(john.email)
print(john.full_name)
print(vars(john))
john.age = 70
print(vars(john))

del john.age
print(vars(john))
john.age = 10
print(vars(john))
john.age = 20
print(vars(john))


class Climber:
    default_grade = "v1"

    def __init__(self, fname, lname, max_grade):
        self.fname = fname
        self.lname = lname
        # assign default and then using setter to add property and get it validated
        self._max_grade = self.default_grade
        self.max_grade = max_grade

    @property
    def max_grade(self):
        return self._max_grade

    @max_grade.setter
    def max_grade(self, new_max_grade):
        if not isinstance(new_max_grade, str):
            print(f"Warning! {new_max_grade} must be a str")
            return
        if not new_max_grade.startswith("v") or not new_max_grade[1:].isdigit():
            print(f"Warning! {new_max_grade} must start with v and end with digits")
            return
        self._max_grade = new_max_grade

    @max_grade.deleter
    def max_grade(self):
        self._max_grade = self.default_grade


john = Climber("john", "smith", "aa")
print(vars(john))
print(john.max_grade)
john.max_grade = "v2"
print(vars(john))
print(john.max_grade)
del john.max_grade
print(vars(john))
print(john.max_grade)


class Soldier:
    def __init__(self, rank, fname, lname):
        self.rank = rank
        self.fname = fname
        self.lname = lname

    @property
    def full_title(self):
        return f"{self.rank.title()} {self.fname.title()} {self.lname.title()}"

    @property
    def short_title(self):
        return f"{self.rank.title()} {self.fname[0].upper()} {self.lname[0].upper()}"


class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if isinstance(new_balance, int) and new_balance >= 0:
            self.balance = new_balance
            return
        raise ValueError("Balance must be positive int")


class Rectangle:
    def __init__(self, height=0, width=0):
        self._height = height
        self._width = width

    @property
    def area(self) -> int:
        return self._height * self._width

    @area.deleter
    def area(self):
        self._width = 0
        self._height = 0
