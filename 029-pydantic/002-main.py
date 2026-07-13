from functools import partial
from datetime import UTC, datetime
import json
from typing import Annotated, Literal
from uuid import UUID, uuid4
from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    HttpUrl,
    SecretStr,
    ValidationError,
    computed_field,
    field_validator,
    model_validator,
)


class User(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        # dont coerce values
        strict=True,
        # allow extra fields
        extra="allow",
        # validate on all assignments
        validate_assignment=True,
        # Makes the data immutable after validation
        # frozen=True
    )

    # uid: int

    # add metadata to type
    # uid: Annotated[int, Field(gt=0)]

    uid: UUID = Field(alias="id", default_factory=uuid4)

    # username: str
    username: Annotated[str, Field(min_length=3, max_length=20)]

    age: Annotated[int, Field(ge=13, le=103)]

    # email: str
    email: EmailStr

    website: HttpUrl | None = None

    password: SecretStr

    bio: str = ""
    is_active: bool = True
    # full_name: str | None = None
    verified_at: datetime | None = None

    first_name: str = ""
    last_name: str = ""
    follower_count: int = 0

    @field_validator("username")
    @classmethod
    def validate_username(cls, v: str) -> str:
        if not v.replace("_", "").isalnum():
            raise ValueError("Username must be alphanumeric (underscores allowed)")
        return v.lower()

    # run the code before valdiation
    @field_validator("website", mode="before")
    @classmethod
    def add_https(cls, v: str | None) -> str | None:
        if v and not v.startswith(("http://", "https://")):
            return f"https://{v}"
        return v

    @computed_field
    @property
    def display_name(self) -> str:
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username

    @computed_field
    @property
    def is_influencer(self) -> bool:
        return self.follower_count >= 10000


class Comment(BaseModel):
    content: str
    author_email: EmailStr
    likes: int = 0


class UserRegistration(BaseModel):
    email: EmailStr
    password: str
    confirm_password: str

    # gets all the fields of model, after all are validated
    @model_validator(mode="after")
    def passwords_match(self) -> "UserRegistration":
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self


try:
    registration = UserRegistration(
        email="CoreyMSchafer@gmail.com",
        password="secret123",
        confirm_password="secret456",
    )
except ValidationError as e:
    print(e)


# user = User(username="john.doe", email="john.doe@email.com", uid=123)
# print(user)
# print(user.username)

# print(user.bio)
# # No revalidation on reassignment by default
# user.bio = 123
# print(user.bio)
# user.bio = "Python developer"

# # returns dict
# print(user.model_dump())
# # returns json string
# print(user.model_dump_json(indent=2))


# try:
#     user = User(
#         username=None,
#         email=123,
#         # type coercion enabled by default
#         uid="123",
#     )
# except ValidationError as e:
#     print(e)


class BlogPost(BaseModel):
    # title: str
    title: Annotated[str, Field(min_length=1, max_length=200)]

    # content: str
    content: Annotated[str, Field(min_length=10)]

    view_count: int = 0
    is_published: bool = False

    # using default_factory instead of [] to create a new list to avoid sharing same instance
    tags: list[str] = Field(default_factory=list)

    # This will create attribute once at class creation and re use it everywhere
    # created_at: datetime = datetime.now(tz=UTC)

    # This will use factory to always create a new version
    # created_at: datetime = Field(default_factory=lambda: datetime.now(tz=UTC))

    # using partial instead of creating lambda
    created_at: datetime = Field(default_factory=partial(datetime.now, tz=UTC))

    # author_id: str | int
    author: User

    status: Literal["draft", "published", "archived"] = "draft"

    slug: Annotated[str, Field(pattern="^[a-zA-Z0-9-]+$")]

    comments: list[Comment] = Field(default_factory=list)


# post = BlogPost(
#     title="Getting Started with Python",
#     content="Here's how to begin...",
#     author_id="12345",
# )
# print(post)


try:
    user = User(
        uid=0,
        username="cs",
        email="JohnDoe@gmail.com",
        age=12,
    )
except ValidationError as e:
    print(e)

user = User(
    username="johndoe1",
    email="JohnDoe@gmail.com",
    age=39,
    password="secret123",
    website="johndoe.com",
)
print(user)
print(user.password.get_secret_value())

user_data = {
    # using alias of id for uid
    "id": "3bc4bf25-1b73-44da-9078-f2bb310c7374",
    "username": "Corey_Schafer",
    "email": "CoreyMSchafer@gmail.com",
    "age": 39,
    "password": "secret123",
    "notes": "Kind've a Karen...",
}
user = User.model_validate_json(json.dumps(user_data))

user.email = "CoreyMSchafer2@gmail.com"

print(user.model_dump_json(indent=2, by_alias=True, exclude=["password"]))
print(user.model_dump_json(indent=2, by_alias=True, include=["username", "email"]))

post_data = {
    "title": "Understanding Pydantic Models",
    "content": "Pydantic makes data validation easy and intuitive...",
    "slug": "understanding-pydantic",
    "author": {
        "username": "coreyms",
        "email": "CoreyMSchafer@gmail.com",
        "age": 39,
        "password": "secret123",
    },
    "comments": [
        {
            "content": "I think I understand nested models now!",
            "author_email": "student@example.com",
            "likes": 25,
        },
        {
            "content": "Can you cover FastAPI next?",
            "author_email": "viewer@example.com",
            "likes": 15,
        },
    ],
}

post = BlogPost(**post_data)

print(post.model_dump_json(indent=2))
