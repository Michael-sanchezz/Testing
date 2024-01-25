grades = {
    'Fred': 90,
    'Sally': 100,
    'Abdul': 100,
    'Julia': 85,
    'Samuel': 80
}
for grade in grades:
    print(grade) # This is just the key!

# Let's print everything
print('Here are all the grades.')
for key in grades:
    print(f'{key} has grade {grades[key]}')