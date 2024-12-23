grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_student = list(students)
sorted_list = sorted(list_student)

gpa_1 = sum(grades[0]) / len(grades[0])
gpa_2 = sum(grades[1]) / len(grades[1])
gpa_3 = sum(grades[2]) / len(grades[2])
gpa_4 = sum(grades[3]) / len(grades[3])
gpa_5 = sum(grades[4]) / len(grades[4])

gpa = [gpa_1, gpa_2, gpa_3, gpa_4, gpa_5]

dict_1 = dict(zip(sorted_list, gpa))

print(dict_1)
