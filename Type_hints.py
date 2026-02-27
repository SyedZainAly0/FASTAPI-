def get_name(firstname: str, lastname: str):
    return f"{firstname.capitalize()} {lastname.capitalize()}"  # added ()

print(get_name("zain", "aly"))  



def get_items_basic(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_e

print(get_items_basic('apple', 2, 1.2, True, b'data'))



def get_items_complex(  names: list[str], scores: tuple[int, int, int], profile: dict[str, str],  active: bool, raw_data: bytes):
    return names, scores, profile, active, raw_data

print(get_items_complex( ["Zain", "Ali"], (90, 85, 88), {"city": "Lahore", "role": "Developer"},True, b"binarydata"))


# Person class
class Person:
    def __init__(self, name: str, age: int, email: str):
        self.name = name
        self.age = age
        self.email = email

def get_person_name(one_person: Person):
    return one_person.name

def get_person_email(one_person: Person):
    return one_person.email

p1 = Person("Zain", 22, "zain@example.com")
print(get_person_name(p1))
print(get_person_email(p1))