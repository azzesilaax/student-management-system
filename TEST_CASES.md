# Student Implementation Class — Test Cases

Objective: Verify the Student class in the existing Student Management System using Python unittest.

Preconditions: Python 3.10 or later; run from the project root. Each test starts with a fresh Student (1001, Deniz Kaya, deniz@example.com) and Course (CS101, Python, capacity 1).

| ID | Test name | Steps / input | Expected result | Actual result | Status |
|---|---|---|---|---|---|
| TC_001 | Student creation | Construct Student with the specified ID, name and email | All attributes match; course list is empty | Attributes match; empty list | PASS |
| TC_002 | Student enrollment | Call student.enroll(course) | Enrollment links student and course; student appears in course; seats = 0 | All assertions satisfied | PASS |
| TC_003 | Get courses | Enroll in CS101 and CS202; call get_courses() | Both courses returned in enrollment order | Both courses returned in order | PASS |
| TC_004 | Duplicate enrollment | Enroll in CS101 twice | ValueError for duplicate; one enrollment remains | Expected exception; one enrollment remains | PASS |
| TC_005 | Full course | Enroll another student in CS101 first, then attempt enrollment | ValueError; target student's course list stays empty; original student remains enrolled | All assertions satisfied | PASS |

## Execution

```bash
python -m unittest discover -s tests -p test_student.py -v
```

To run all original and new tests:

```bash
python -m unittest discover -s tests -v
```

See TEST_RESULTS.txt for the actual combined test run. Original implementation files are unchanged.
