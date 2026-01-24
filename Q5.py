
students: int = int(input("how many students are there ?"))

while students <= 0:
    students = int(input("invalid input try again"))

index: int = 1
grade_sum: int = 0

while index <= students:
    print("enter a grade of student number ", index)
    grade: int = int(input())
    if 0 <= grade <= 100:
        grade_sum += grade
        index += 1
    else:
        print("invalid input")

average: float = grade_sum / students
print("the average is ", average)
