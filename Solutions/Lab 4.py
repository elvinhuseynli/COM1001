x = input().split()
number_of_students = int(x[0])
lab_count = int(x[1])
homework_count = int(x[2])
student_id = []
name = []
surname = []
lab_avrg_grade = []
homework_avrg_grade = []
average_grades = []
wanted_numbers = []
o=0
midterm_grade = []
final_grade = []

for t in range(1,number_of_students+1):
    y = input().split()
    student_id.append(y[0])
    name.append(y[1])
    surname.append(y[2])
    exam_type = 4
    lab_avrg_grades = 0
    homework_avrg_grades = 0
    average_grade = 0
    lab_grades = []
    homework_grades = []
    while '<' in y and '>' in y and exam_type != 0:
        if exam_type == 4:
            for i in range(y.index('<')+1,y.index('>')):
                lab_grades.append(int(y[i]))
                if len(lab_grades) != lab_count:
                    lab_grades.append(0)
            y.remove('<')
            y.remove('>')
            exam_type -= 1
        if exam_type == 3:
            for i in range(y.index('<')+1,y.index('>')):
                homework_grades.append(int(y[i]))
                if len(homework_grades) != homework_count:
                    homework_grades.append(0)
            y.remove('<')
            y.remove('>')
            exam_type -= 1
        if exam_type == 2:
            for i in range(y.index('<')+1,y.index('>')):
                midterm_grade.append(int(y[i]))
            y.remove('<')
            y.remove('>')
            exam_type -= 1
        if exam_type == 1:
            for i in range(y.index('<')+1,y.index('>')):
                final_grade.append(int(y[i]))
            y.remove('<')
            y.remove('>')
            exam_type -= 1
    else:
        pass
    for v in lab_grades:
        lab_avrg_grades+=v
    for u in homework_grades:
        homework_avrg_grades+=u
    homework_avrg_grade.append(homework_avrg_grades/homework_count)
    lab_avrg_grade.append(lab_avrg_grades/lab_count)
    if len(midterm_grade) == o:
        midterm_grade.append(0)
    if len(final_grade) == o:
        final_grade.append(0)
    average_grade+=(homework_avrg_grade[o])/10 + (lab_avrg_grade[o])/10 + (midterm_grade[o])/10 + (final_grade[o])*8/10
    average_grades.append(average_grade)
    o+=1
z=input().split()
for d in z:
    for m in student_id:
        if bool(z) == True:
            if d==m:
                print(name[student_id.index(m)] + ' ' + surname[student_id.index(m)] + ' ' + str("{:.2f}".format(average_grades[student_id.index(m)])))
                break
            elif d!=m and d==z[-1] and m==student_id[-1]:
               print(None)
        if bool(z) == False:
            print('None')
