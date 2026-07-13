# def create_user(username, email, age):
#     if not isinstance(username, str):
#         raise TypeError("Username must be a string")
#     if not isinstance(email, str):
#         raise TypeError("Email must be a string")
#     if not isinstance(age, int):
#         raise TypeError("Age must be a integer")

#     return {"username": username, "email": email, "age": age}


# user1 = create_user("test1", "test1@example.com", 38)
# print(user1)

# user2 = create_user("test2", None, "old")
# print(user2)

from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    age: int


# We have to use keyword arguments
user1 = User(username="test1", email="test1@example.com", age=38)
print(user1)

user2 = User(username="test2", email=None, age="old")
print(user2)
