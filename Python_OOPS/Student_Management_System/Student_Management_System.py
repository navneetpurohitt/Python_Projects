class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def update_grade(self, new_grade):
        self.grade = new_grade

    def display_info(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}")


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age, grade):
        if student_id in self.students:
            print("Student ID already exists.")
        else:
            self.students[student_id] = Student(student_id, name, age, grade)
            print("Student added successfully.")

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("Student removed successfully.")
        else:
            print("Student ID not found.")

    def update_student_grade(self, student_id, new_grade):
        if student_id in self.students:
            self.students[student_id].update_grade(new_grade)
            print("Grade updated successfully.")
        else:
            print("Student ID not found.")

    def display_all_students(self):
        if not self.students:
            print("No students in the system.")
        else:
            for student in self.students.values():
                student.display_info()


# Example usage
if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.add_student(1, "Alice", 20, "A")
    sms.add_student(2, "Bob", 22, "B")
    sms.display_all_students()
    sms.update_student_grade(1, "A+")
    sms.remove_student(2)
    sms.display_all_students()