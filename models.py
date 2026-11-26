from dataclasses import dataclass, field


@dataclass
class Student:
    student_id: int
    name: str
    email: str
    enrollments: list = field(default_factory=list, repr=False)

    def enroll(self, course):
        """Register this student for a course."""
        if any(enrollment.course == course for enrollment in self.enrollments):
            raise ValueError(f"{self.name} is already enrolled in {course.title}.")

        enrollment = Enrollment(student=self, course=course)
        course.add_enrollment(enrollment)
        self.enrollments.append(enrollment)
        return enrollment

    def get_courses(self):
        return [enrollment.course for enrollment in self.enrollments]


@dataclass
class Instructor:
    instructor_id: int
    name: str
    email: str
    courses: list = field(default_factory=list, repr=False)

    def assign_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.instructor = self


@dataclass
class Course:
    course_id: str
    title: str
    capacity: int
    instructor: Instructor | None = None
    enrollments: list = field(default_factory=list, repr=False)

    def __post_init__(self):
        if self.capacity <= 0:
            raise ValueError("Course capacity must be greater than zero.")

    def add_enrollment(self, enrollment):
        if len(self.enrollments) >= self.capacity:
            raise ValueError(f"{self.title} is full.")
        self.enrollments.append(enrollment)

    def get_students(self):
        return [enrollment.student for enrollment in self.enrollments]

    def available_seats(self):
        return self.capacity - len(self.enrollments)


@dataclass
class Enrollment:
    student: Student
    course: Course
    status: str = "Active"

    def cancel(self):
        if self in self.student.enrollments:
            self.student.enrollments.remove(self)
        if self in self.course.enrollments:
            self.course.enrollments.remove(self)
        self.status = "Cancelled"
