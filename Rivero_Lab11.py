grades = []
passed = []

    
while True:
    grade = input("Please enter your grade: ")
    
    if grade.lower() == 'done':
        break
    elif not grade.isdigit():
        print("Please enter a numeric grade.")
    else:
        grade = int(grade)
        if (grade <= 40):
            print("Invalid input of grades")
            continue
        elif (grade >= 101):
            print("Invalid input of grades")
            continue
        grades.append(grade)
        if grade >= 75:
            passed.append(grade)
            
if grades: 
        average = sum(grades) / len(grades)
        passingpercent = (len(passed)/ len(grades)) * 100
        print(f"The average is: {average:.2f}")
        print(f"The percentage of grades that passed is: {passingpercent:.2f}%")
        print(f"The student who have passed: {len (passed)} ")
        print(f"Grades: {passed:} ")
else:
    print("No grades were entered")
        