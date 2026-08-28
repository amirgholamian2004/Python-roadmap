students = [{"name": "Ali", "grades": [18, 15, 19]}, {"name": "Sara", "grades": [20, 20, 17]},
{"name": "Reza", "grades": [12, 14, 13]}]

average = {}
unique_grades = set()
for student in students:
    name = student["name"]
    grades = student["grades"]
    avg = round(sum(grades) / len(grades), 1)
    average[name] = avg
    all_grades = set(grades)
    unique_grades.update(all_grades)

best_score = 0
for key, value in average.items():
    if value > best_score:
        best_score = value
        best_key = key

print('average:', average)
print('best score is:', best_score)
print('all the grades together:', unique_grades)
print('best student is:', (best_key, best_score))
