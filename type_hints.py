'''
# without type hints

def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

'''

def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

# print(get_full_name("john", "doe"))

'''
my_bytes = bytes([104, 101, 108, 108, 111])
for byte in my_bytes:
    print(byte)
'''

'''
def process_items(items: list[str]):
    for item in items:
        print(item)
'''

'''
def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s
'''

'''
from typing import Optional

def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")
        
'''

# Pydantic

from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    signup_ts: datetime | None = None
    friends: list[int] = []

external_data = {
    "id": "123",
    "name": "Jhon Doe",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"]
}

user = User(**external_data)
print(type(user))
print(user.id)