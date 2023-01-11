# tamrin 6-6
list_score_students = []

numbers_students = int(input("How many number do you student? "))

for i in range(0, numbers_students):
    score_students = float(input("score_students " + str(i + 1) + ": "))
    list_score_students.append(score_students)
print(list_score_students)
max_score = max(list_score_students)
print('max_score', max_score)
min_score = min(list_score_students)
print("min_score", min_score)
