# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))

exam_three = int(input("Input exam grade three: "))

grades=(exam_one + exam_two + exam_three)
avg=grades/3
print("Average:",avg)

def find_grades(grades):
    if avg>=90:
        return "A"
    elif avg>=80 and avg<=89:
        return "B"
    elif avg>=70 and avg<=79:
        return "C"
    elif avg>=60 and avg<=69:
        return "D"
    else:
        return "F"
Grade=(find_grades(grades))
print("Grade:",Grade)


if find_grades(grades)=="F":
    print("Student is failing.")
else:
    print("Student is passing.")
