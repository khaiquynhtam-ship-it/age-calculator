from age import calculate_age, is_adult

birth_year = int(input('Enter your birth year: '))
age = calculate_age(birth_year)

print(f'Your age is: {age}')
print('Status:', 'Adult' if is_adult(age) else 'Minor')
