from datetime import datetime


def calculate_age(birth_year):
    return datetime.now().year - birth_year


def is_adult(age):
    return age >= 18
