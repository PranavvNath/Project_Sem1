# Student Marks Analyser
# Class project

import numpy as np
import random

subjects = ["Maths", "Science", "English", "Hindi", "Computer"]
names = []
marks = []

print("===== STUDENT MARKS ANALYSER =====")

choice = 0
while choice != 8:
    print()
    print("1. Enter student marks")
    print("2. Fill random marks (for testing)")
    print("3. Show report card of all students")
    print("4. Subject wise analysis")
    print("5. Rank list")
    print("6. Class topper")
    print("7. Pass / Fail count")
    print("8. Exit")
    choice = int(input("Enter your choice: "))

    # entering marks by hand
    if choice == 1:
        n = int(input("How many students? "))
        for i in range(n):
            name = input("Enter name of student " + str(i + 1) + ": ")
            names.append(name)
            student_marks = []
            for s in subjects:
                m = int(input("  Marks in " + s + " (out of 100): "))
                while m < 0 or m > 100:
                    print("  Marks should be between 0 and 100")
                    m = int(input("  Enter marks in " + s + " again: "))
                student_marks.append(m)
            marks.append(student_marks)

    # random marks so we dont have to type everything while testing
    elif choice == 2:
        n = int(input("How many students? "))
        for i in range(n):
            names.append("Student" + str(len(names) + 1))
            student_marks = []
            for s in subjects:
                student_marks.append(random.randint(20, 100))
            marks.append(student_marks)
        print(n, "students added with random marks")

    elif choice >= 3 and choice <= 7 and len(names) == 0:
        print("No data yet! Enter marks first (option 1 or 2)")

    # report card
    elif choice == 3:
        arr = np.array(marks)
        for i in range(len(names)):
            total = np.sum(arr[i])
            per = total / len(subjects)

            if np.min(arr[i]) < 33:
                grade = "F"
            elif per >= 90:
                grade = "A+"
            elif per >= 75:
                grade = "A"
            elif per >= 60:
                grade = "B"
            elif per >= 45:
                grade = "C"
            else:
                grade = "D"

            print()
            print("Name:", names[i])
            for j in range(len(subjects)):
                print("  ", subjects[j], ":", arr[i][j])
            print("  Total      :", total, "/", len(subjects) * 100)
            print("  Percentage :", round(per, 2), "%")
            print("  Grade      :", grade)
            if grade == "F":
                print("  Result     : FAIL")
            else:
                print("  Result     : PASS")

    # subject wise analysis
    elif choice == 4:
        arr = np.array(marks)
        for j in range(len(subjects)):
            col = arr[:, j]
            highest = col[0]
            top_name = names[0]
            for i in range(len(col)):
                if col[i] > highest:
                    highest = col[i]
                    top_name = names[i]
            print()
            print(subjects[j])
            print("  Average :", round(np.mean(col), 2))
            print("  Highest :", highest, "by", top_name)
            print("  Lowest  :", np.min(col))

    # rank list using bubble sort
    elif choice == 5:
        arr = np.array(marks)
        rank_names = []
        totals = []
        for i in range(len(names)):
            rank_names.append(names[i])
            totals.append(np.sum(arr[i]))

        for i in range(len(totals)):
            for j in range(len(totals) - 1 - i):
                if totals[j] < totals[j + 1]:
                    totals[j], totals[j + 1] = totals[j + 1], totals[j]
                    rank_names[j], rank_names[j + 1] = rank_names[j + 1], rank_names[j]

        print()
        print("RANK  NAME  TOTAL")
        for i in range(len(totals)):
            print(i + 1, " ", rank_names[i], " ", totals[i])

    # topper
    elif choice == 6:
        arr = np.array(marks)
        top = 0
        for i in range(len(names)):
            if np.sum(arr[i]) > np.sum(arr[top]):
                top = i
        print()
        print("Class topper is", names[top])
        print("Total marks:", np.sum(arr[top]))
        print("Percentage:", round(np.mean(arr[top]), 2), "%")

    # pass fail count
    elif choice == 7:
        arr = np.array(marks)
        passed = 0
        failed = 0
        for i in range(len(names)):
            if np.min(arr[i]) < 33:
                failed = failed + 1
            else:
                passed = passed + 1
        print()
        print("Total students:", len(names))
        print("Passed:", passed)
        print("Failed:", failed)
        print("Pass percentage:", round(passed / len(names) * 100, 2), "%")

    elif choice == 8:
        print("Thank you! Bye")

    else:
        print("Wrong choice, try again")
# Student Marks Analyser
# Class project

import numpy as np
import random

subjects = ["Maths", "Science", "English", "Hindi", "Computer"]
names = []
marks = []

print("===== STUDENT MARKS ANALYSER =====")

choice = 0
while choice != 8:
    print()
    print("1. Enter student marks")
    print("2. Fill random marks (for testing)")
    print("3. Show report card of all students")
    print("4. Subject wise analysis")
    print("5. Rank list")
    print("6. Class topper")
    print("7. Pass / Fail count")
    print("8. Exit")
    choice = int(input("Enter your choice: "))

    # entering marks by hand
    if choice == 1:
        n = int(input("How many students? "))
        for i in range(n):
            name = input("Enter name of student " + str(i + 1) + ": ")
            names.append(name)
            student_marks = []
            for s in subjects:
                m = int(input("  Marks in " + s + " (out of 100): "))
                while m < 0 or m > 100:
                    print("  Marks should be between 0 and 100")
                    m = int(input("  Enter marks in " + s + " again: "))
                student_marks.append(m)
            marks.append(student_marks)

    # random marks so we dont have to type everything while testing
    elif choice == 2:
        n = int(input("How many students? "))
        for i in range(n):
            names.append("Student" + str(len(names) + 1))
            student_marks = []
            for s in subjects:
                student_marks.append(random.randint(20, 100))
            marks.append(student_marks)
        print(n, "students added with random marks")

    elif choice >= 3 and choice <= 7 and len(names) == 0:
        print("No data yet! Enter marks first (option 1 or 2)")

    # report card
    elif choice == 3:
        arr = np.array(marks)
        for i in range(len(names)):
            total = np.sum(arr[i])
            per = total / len(subjects)

            if np.min(arr[i]) < 33:
                grade = "F"
            elif per >= 90:
                grade = "A+"
            elif per >= 75:
                grade = "A"
            elif per >= 60:
                grade = "B"
            elif per >= 45:
                grade = "C"
            else:
                grade = "D"

            print()
            print("Name:", names[i])
            for j in range(len(subjects)):
                print("  ", subjects[j], ":", arr[i][j])
            print("  Total      :", total, "/", len(subjects) * 100)
            print("  Percentage :", round(per, 2), "%")
            print("  Grade      :", grade)
            if grade == "F":
                print("  Result     : FAIL")
            else:
                print("  Result     : PASS")

    # subject wise analysis
    elif choice == 4:
        arr = np.array(marks)
        for j in range(len(subjects)):
            col = arr[:, j]
            highest = col[0]
            top_name = names[0]
            for i in range(len(col)):
                if col[i] > highest:
                    highest = col[i]
                    top_name = names[i]
            print()
            print(subjects[j])
            print("  Average :", round(np.mean(col), 2))
            print("  Highest :", highest, "by", top_name)
            print("  Lowest  :", np.min(col))

    # rank list using bubble sort
    elif choice == 5:
        arr = np.array(marks)
        rank_names = []
        totals = []
        for i in range(len(names)):
            rank_names.append(names[i])
            totals.append(np.sum(arr[i]))

        for i in range(len(totals)):
            for j in range(len(totals) - 1 - i):
                if totals[j] < totals[j + 1]:
                    totals[j], totals[j + 1] = totals[j + 1], totals[j]
                    rank_names[j], rank_names[j + 1] = rank_names[j + 1], rank_names[j]

        print()
        print("RANK  NAME  TOTAL")
        for i in range(len(totals)):
            print(i + 1, " ", rank_names[i], " ", totals[i])

    # topper
    elif choice == 6:
        arr = np.array(marks)
        top = 0
        for i in range(len(names)):
            if np.sum(arr[i]) > np.sum(arr[top]):
                top = i
        print()
        print("Class topper is", names[top])
        print("Total marks:", np.sum(arr[top]))
        print("Percentage:", round(np.mean(arr[top]), 2), "%")

    # pass fail count
    elif choice == 7:
        arr = np.array(marks)
        passed = 0
        failed = 0
        for i in range(len(names)):
            if np.min(arr[i]) < 33:
                failed = failed + 1
            else:
                passed = passed + 1
        print()
        print("Total students:", len(names))
        print("Passed:", passed)
        print("Failed:", failed)
        print("Pass percentage:", round(passed / len(names) * 100, 2), "%")

    elif choice == 8:
        print("Thank you! Bye")

    else:

        print("Wrong choice, try again")