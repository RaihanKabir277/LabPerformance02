

students = [
    ("Raihan", 20, 85),
    ("Kabir", 22, 90),
    ("Alif", 21, 78),
    ("Hridoy", 19, 92),
    ("Jahid", 20, 88)
]

SortByGrade = sorted(students, key=lambda x: x[2])


print("Students sorted by grade:")
for student in SortByGrade:
    print(student)