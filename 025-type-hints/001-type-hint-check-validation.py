from pydantic import validate_call


# uses type hint to do auto type checking
@validate_call
def create_user(first_name: str, last_name: str, age: int) -> dict:
    email = f"{first_name.lower()}_{last_name.lower()}@example.com"

    # data validation manually
    # if not isinstance(first_name, str):
    #     raise TypeError('first_name must be a string')
    # if not isinstance(last_name, str):
    #     raise TypeError('last_name must be a string')
    # if not isinstance(age, int):
    #     raise TypeError('age must be an integer')

    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "email": email,
    }


user_1: dict = create_user("John", "Doe", 38)
print(user_1)


# Type hints just gives hints, no static type checking
# Run with some external tool to get static type checking

# mypy 025-type-hints/001-type-hints.py
# 025-type-hints/001-type-hints.py:20: error: Argument 3 to "create_user" has incompatible type "str"; expected "int"  [arg-type]
# Found 1 error in 1 file (checked 1 source file)
user_2: dict = create_user("John", "Doe", "thirty-eight")
print(user_2)
