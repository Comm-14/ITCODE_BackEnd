students = {'Schultz', 'Django', 'Brunhilde', 'Fritz'}
employees = {'Schultz', 'Django', 'Calvin', 'Butch', 'Fritz'}

# Все люди
all_people_1 = students.union(employees)
all_people_2 = students | employees

print("Все люди (способ 1):", all_people_1)
print("Все люди (способ 2):", all_people_2)

# Одовременно учится и работает
both_education_and_work_1 = students.intersection(employees)
both_education_and_work_2 = students & employees
print("Те, кто одновременно учится и работает (способ 1):", both_education_and_work_1)
print("Те, кто одновременно учится и работает (способ 2):", both_education_and_work_2)

# Только работает
only_work_1 = employees.difference(students)
only_work_2 = employees - students
print("Те, кто только работает, но не учится (способ 1):", only_work_1)
print("Те, кто только работает, но не учится (способ 2):", only_work_2)

# Либо либо но не одновременно
either_education_or_work_1 = students.symmetric_difference(employees)
either_education_or_work_2 = students ^ employees

print("Те, кто либо учится, либо работает, но не одновременно (способ 1):", either_education_or_work_1)
print("Те, кто либо учится, либо работает, но не одновременно (способ 2):", either_education_or_work_2)