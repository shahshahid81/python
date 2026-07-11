from dataclasses import dataclass
import random
import requests
from typing import Any, NewType, Optional, TypeVar, TypedDict

name: str = "John"
age: int = 38

# Type check error when using mypy
# age = 'one'


# Optional is the verbose syntax
# def create_user(first_name: str, last_name: str, age: Optional[int] = None) -> dict:

# type is optional
# note that both types are same and user passed HSL values as RGB, there won't be any error
# type RGB = tuple[int, int, int]
# type HSL = tuple[int, int, int]

RGB = NewType("RGB", tuple[int, int, int])
HSL = NewType("HSL", tuple[int, int, int])


# class User(TypedDict):
#     first_name: str
#     last_name: str
#     email: str
#     age: int | None
#     fav_color: RGB | None


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    age: int | None = None
    fav_color: RGB | None = None


# type User = dict[str, str | int | RGB | None]


# "|" is used for union
def create_user(
    first_name: str,
    last_name: str,
    age: int | None = None,
    fav_color: RGB | None = None,
) -> User:
    # ) -> dict[str, str | int | None]:

    # implicit str type hint
    email = f"{first_name.lower()}_{last_name.lower()}@example.com"

    # return {
    #     "first_name": first_name,
    #     "last_name": last_name,
    #     "age": age,
    #     "email": email,
    #     "fav_color": fav_color,
    # }

    return User(
        first_name=first_name,
        last_name=last_name,
        age=age,
        email=email,
        fav_color=fav_color,
    )


# using any doesn't give type hinting benefits like auto complete and type checking
# def random_choice(items: list[Any]) -> Any:

# Old way of declaring generic type
# T = TypeVar("T")
# def random_choice(items: list[T]) -> T:

# declaring generic type
def random_choice[T](items: list[T]) -> T:
    return random.choice(items)

# user_1 has RGB values and user_2 has HSL Values, but since we only used RGB as type, HSL value was also accepted due to same structure
# user_1: dict = create_user("John", "Doe", age=38, fav_color=(0, 0, 0))
# user_2: dict = create_user("John", "Doe", fav_color=(206, 10, 48))

user_1 = create_user("John", "Doe", age=38, fav_color=RGB((0, 0, 0)))
user_2 = create_user("John", "Doe", fav_color=RGB(((206, 10, 48))))

print(user_1)
print(user_2)

users = [user_1, user_2]
rando_user = random_choice(users)
print(rando_user)

emails = [user.email for user in users]
rando_email = random_choice(emails)
print(rando_email)


# run the install command for type specifically
# pip install types-requests
resp = requests.get('https://example.com', timeout=5)
status = resp.status_code
print(status)
# status = 'ok'
# print(status)