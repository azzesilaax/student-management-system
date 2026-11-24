from student_management.models import Student, Instructor, Course


def main():
    # Create an instructor and courses
    instructor = Instructor(1, "Dr. Ada Yilmaz", "ada@example.com")
    python_course = Course("CS101", "Introduction to Python", capacity=2)
    database_course = Course("CS202", "Database Systems", capacity=3)

    instructor.assign_course(python_course)
    instructor.assign_course(database_course)

    # Create students
    student1 = Student(1001, "Deniz Kaya", "deniz@example.com")
    student2 = Student(1002, "Ece Demir", "ece@example.com")

    # Enroll students
    student1.enroll(python_course)
    student1.enroll(database_course)
    student2.enroll(python_course)

    print("STUDENT MANAGEMENT SYSTEM")
    print("-------------------------")
    for student in (student1, student2):
        course_names = ", ".join(course.title for course in student.get_courses())
        print(f"{student.name}: {course_names}")

    print(f"\nInstructor: {instructor.name}")
    print(f"Courses taught: {len(instructor.courses)}")
    print(f"Available seats in {python_course.title}: "
          f"{python_course.available_seats()}")


if __name__ == "__main__":
    main()
