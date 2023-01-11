# tamrin 6-2
# asami daneshjoyan vared shavad va az metodhaaee list estefadeh shavad
list_name_students = []
name_student = input("Enter the names of the students:")  # afsaneh dorsa ala fatemeh
list_name_students = name_student.strip().lower().split()
print(list_name_students)
list_name_students.sort()
print(list_name_students)
list_name_students.append("nastarn")
print(list_name_students)
list_name_students.extend(['reza', 'ali'])
print(list_name_students)
list_name_students.remove('ali')
print(list_name_students)
list_name_students.pop()
print(list_name_students)
print('tedad_list = ', len(list_name_students))
