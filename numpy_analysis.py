import numpy as np
import numpy as np

marks = np.array([85, 78, 92, 67, 88])

print(marks)
print(type(marks))
print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))



students = np.array([
    [85, 78, 92],
    [72, 81, 75],
    [91, 88, 95],
    [64, 70, 68],
    [79, 85, 82]
])

print("Student Marks:")
print(students)

print("\nShape:", students.shape)

print("\nFirst student:")
print(students[0])

print("\nMaths marks:")
print(students[:, 0])

print("\nEnglish marks:")
print(students[:, 1])

print("\nComputer marks:")
print(students[:, 2])

print("\nSubject-wise average:")  
print(np.mean(students, axis=0))

print("\nStudent-wise average:")
print(np.mean(students, axis=1))

student_average = np.mean(students, axis=1)

print("\nHighest student average:")
print(np.max(student_average))

print("\nLowest student average:")
print(np.min(student_average))

print("\nOverall average:")
print(np.mean(students))

student_average = np.mean(students, axis=1)

print("\nStudents with average above 80:")
print(students[student_average > 80]) #boolean 

print("\nSorted student averages:")
print(np.sort(student_average))

# highest topper ke marks
topper_index = np.argmax(student_average)

print("\nTopper:")
print("Student", topper_index + 1)
print("Average:", student_average[topper_index])