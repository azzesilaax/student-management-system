import unittest

from student_management.models import Student, Instructor, Course


class StudentManagementTests(unittest.TestCase):
    def setUp(self):
        self.instructor = Instructor(1, "Ada Yilmaz", "ada@example.com")
        self.course = Course("CS101", "Python", capacity=1)
        self.instructor.assign_course(self.course)
        self.student = Student(1001, "Deniz Kaya", "deniz@example.com")

    def test_student_can_enroll(self):
        self.student.enroll(self.course)
        self.assertEqual(len(self.student.get_courses()), 1)
        self.assertEqual(self.course.available_seats(), 0)

    def test_duplicate_enrollment_is_rejected(self):
        self.student.enroll(self.course)
        with self.assertRaises(ValueError):
            self.student.enroll(self.course)

    def test_course_capacity_is_enforced(self):
        self.student.enroll(self.course)
        another = Student(1002, "Ece Demir", "ece@example.com")
        with self.assertRaises(ValueError):
            another.enroll(self.course)

    def test_instructor_can_be_assigned_to_course(self):
        self.assertIn(self.course, self.instructor.courses)
        self.assertIs(self.course.instructor, self.instructor)


if __name__ == "__main__":
    unittest.main()
