# tamrin 6-2
# مثال: 10 عدد از کاربر گزفته شود-این اعداد به لیست تبدیل شود و با کمک متودها ببه صورت نزولی نمایش داده شود
print("روش اول")
numbers = input("Please enternumbers::")  # 90 40 39 28 67 43 65 29 39 30
# مشکل 1: خط بالا مشکل داشتم زمانی که int قبل input میزارم اررو میده میخوام که عدد صحیح در نظر بگیرد
list_numbers = numbers.split()
print(list_numbers)
list_numbers.sort()
print(list_numbers)
list_numbers.reverse()
print(list_numbers)

print("--------------------------------")
#-----------------------------------------------------------------------------

print("روش دوم")
number_list = []
n = int(input("How many number do you have? "))

for i in range(0, n):
    item = int(input("Enter number "+ str(i+1) + ": "))
    number_list.append(item)
print("User list is ", number_list)
number_list.sort()
print("User list is ", number_list)
number_list.reverse()
print("User list is ", number_list)




