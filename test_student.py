import unittest
from student_management.models import Student, Course


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student(1001, 'Deniz Kaya', 'deniz@example.com')
        self.course = Course('CS101', 'Python', capacity=1)

    def test_student_creation(self):
        self.assertEqual(self.student.student_id, 1001)
        self.assertEqual(self.student.name, 'Deniz Kaya')
        self.assertEqual(self.student.email, 'deniz@example.com')
        self.assertEqual(self.student.get_courses(), [])

    def test_student_enrollment(self):
        enrollment = self.student.enroll(self.course)
        self.assertIs(enrollment.student, self.student)
        self.assertIs(enrollment.course, self.course)
        self.assertIn(self.student, self.course.get_students())
        self.assertEqual(self.course.available_seats(), 0)

    def test_get_courses(self):
        another_course = Course('CS202', 'Database Systems', capacity=2)
        self.student.enroll(self.course)
        self.student.enroll(another_course)
        self.assertEqual(self.student.get_courses(), [self.course, another_course])

    def test_duplicate_enrollment(self):
        self.student.enroll(self.course)
        with self.assertRaisesRegex(ValueError, 'already enrolled'):
            self.student.enroll(self.course)
        self.assertEqual(len(self.student.enrollments), 1)

    def test_full_course(self):
        another_student = Student(1002, 'Ece Demir', 'ece@example.com')
        another_student.enroll(self.course)
        with self.assertRaisesRegex(ValueError, 'is full'):
            self.student.enroll(self.course)
        self.assertEqual(self.student.get_courses(), [])
        self.assertEqual(self.course.get_students(), [another_student])


if __name__ == '__main__':
    unittest.main()
