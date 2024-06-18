import random
from string import ascii_letters, ascii_lowercase, digits


def generate_name():
    letters_part = "".join(random.choices(ascii_lowercase, k=5))
    number_part = "".join(random.choices(digits, k=3))
    return f"{letters_part}_{number_part}"


def generate_email(name):
    domain = "".join(random.choices(ascii_lowercase, k=4))
    return f"{name}@{domain}.ru"


def generate_password():
    return "".join(random.choices(ascii_letters + digits, k=8))

