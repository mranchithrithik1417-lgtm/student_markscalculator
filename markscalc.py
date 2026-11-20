def calculate_marks():
    num_subjects = int(input("Enter the number of subjects: "))
    total_marks = 0
    max_marks_per_subject = 100

    for i in range(1, num_subjects + 1):
        marks = float(input(f"Enter marks for subject {i}: "))
        total_marks += marks

    max_total = num_subjects * max_marks_per_subject
    percentage = (total_marks / max_total) * 100

    print(f"\nTotal Marks: {total_marks} / {max_total}")
    print(f"Percentage: {percentage:.2f}%")

if __name__ == "__main__":
    calculate_marks()
