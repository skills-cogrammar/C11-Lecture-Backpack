# ==========================
# Model: Student and Course
# ==========================
class Course:
    """
    Represents a course in the enrollment system.
    Attributes:
        course_id (str): Unique identifier for the course.
        course_name (str): Name of the course.
        capacity (int): Maximum number of students that can enroll in the course.
        enrolled_students (list): List of students enrolled in the course.
    """
    def __init__(self, course_id, course_name, capacity):
        """
        Initializes a Course object.
        Args:
            course_id (str): Unique identifier for the course.
            course_name (str): Name of the course.
            capacity (int): Maximum number of students that can enroll in the course.
        """
        self.course_id = course_id
        self.course_name = course_name
        self.capacity = capacity
        self.enrolled_students = []  # List to store enrolled students

    def enroll_student(self, student):
        """
        Enrolls a student in the course if there is available capacity.
        Args:
            student (Student): The student to enroll.
        Returns:
            bool: True if enrollment is successful, False if the course is full.
        """
        if len(self.enrolled_students) < self.capacity:
            self.enrolled_students.append(student)
            return True  # Enrollment successful
        else:
            return False  # Course is full

    def drop_student(self, student):
        """
        Drops a student from the course if they are enrolled.
        Args:
            student (Student): The student to drop.
        Returns:
            bool: True if the student is successfully dropped, False if the student is not enrolled.
        """
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            return True  # Drop successful
        else:
            return False  # Student not enrolled

    def view_roster(self):
        """
        Returns a list of names of students enrolled in the course.
        Returns:
            list: List of student names.
        """
        return [student.name for student in self.enrolled_students]


class Student:
    """
    Represents a student in the enrollment system.
    Attributes:
        student_id (int): Unique identifier for the student.
        name (str): Name of the student.
        email (str): Email address of the student.
        enrolled_courses (list): List of courses the student is enrolled in.
    """
    def __init__(self, student_id, name, email):
        """
        Initializes a Student object.
        Args:
            student_id (int): Unique identifier for the student.
            name (str): Name of the student.
            email (str): Email address of the student.
        """
        self.student_id = student_id
        self.name = name
        self.email = email
        self.enrolled_courses = []  # List to store enrolled courses

    def enroll_in_course(self, course):
        """
        Enrolls the student in a course if there is available capacity.
        Args:
            course (Course): The course to enroll in.
        Returns:
            str: A message indicating whether the enrollment was successful or not.
        """
        if course.enroll_student(self):
            self.enrolled_courses.append(course)
            return f"{self.name} enrolled in {course.course_name}."
        else:
            return f"Failed to enroll {self.name} in {course.course_name}. Course is full."

    def drop_course(self, course):
        """
        Drops the student from a course if they are enrolled.
        Args:
            course (Course): The course to drop.
        Returns:
            str: A message indicating whether the drop was successful or not.
        """
        if course.drop_student(self):
            self.enrolled_courses.remove(course)
            return f"{self.name} dropped {course.course_name}."
        else:
            return f"Failed to drop {self.name} from {course.course_name}. Student not enrolled."

    def view_enrolled_courses(self):
        """
        Returns a list of course IDs and names for the courses the student is enrolled in.
        Returns:
            list: List of strings in the format "Course ID: Course Name".
        """
        enrolled_course_names = []
        for course in self.enrolled_courses:
            enrolled_course_names.append(f"{course.course_id}: {course.course_name}")
        return enrolled_course_names


# ==========================
# View: Student Interface
# ==========================
class StudentView:
    """
    Handles the user interface for the student, including displaying forms and course information.
    """
    def __init__(self):
        pass

    def render_available_courses(self, courses):
        """
        Displays a list of available courses.
        Args:
            courses (list): List of Course objects.
        """
        print("=== Available Courses ===")
        if courses:
            for course in courses:
                print(f"Course ID: {course.course_id}, Name: {course.course_name}")
        else:
            print("No courses available.")

    def render_enrollment_form(self):
        """
        Displays the enrollment form and collects the course ID from the user.
        Returns:
            str: The course ID entered by the user.
        """
        print("=== Enrollment Form ===")
        course_id = input("Enter Course ID: ")
        return course_id

    def render_drop_form(self):
        """
        Displays the drop course form and collects the course ID from the user.
        Returns:
            str: The course ID entered by the user.
        """
        print("=== Drop Course Form ===")
        course_id = input("Enter Course ID: ")
        return course_id

    def render_enrolled_courses(self, courses):
        """
        Displays the list of courses the student is enrolled in.
        Args:
            courses (list): List of course names.
        """
        print("=== Enrolled Courses ===")
        if courses:
            for course in courses:
                print(f"- {course}")
        else:
            print("No courses enrolled.")


# ==========================
# Controller: Student Logic
# ==========================
class StudentController:
    """
    Manages the logic for student-related actions, such as enrolling in and dropping courses.
    Attributes:
        student (Student): The student interacting with the system.
        courses (list): List of available Course objects.
        view (StudentView): The user interface for the student.
    """
    def __init__(self, student, courses):
        """
        Initializes a StudentController object.
        Args:
            student (Student): The student interacting with the system.
            courses (list): List of available Course objects.
        """
        self.student = student
        self.courses = courses
        self.view = StudentView()

    def handle_show_available_courses_request(self):
        """
        Handles the request to show available courses by calling the appropriate view method.
        """
        self.view.render_available_courses(self.courses)

    def handle_enrollment_request(self):
        """
        Handles the enrollment request by collecting the course ID from the user,
        finding the course, and enrolling the student if possible.
        """
        course_id = self.view.render_enrollment_form()
        
        # Explicitly search for the course
        course = None
        for course_item in self.courses:
            if course_item.course_id == course_id:
                course = course_item
                break
        
        if course:
            result = self.student.enroll_in_course(course)
            print(result)
        else:
            print("Course not found.")

    def handle_drop_request(self):
        """
        Handles the drop request by collecting the course ID from the user,
        finding the course, and dropping the student if possible.
        """
        course_id = self.view.render_drop_form()
        
        # Explicitly search for the course
        course = None
        for course_item in self.courses:
            if course_item.course_id == course_id:
                course = course_item
                break
        
        if course:
            result = self.student.drop_course(course)
            print(result)
        else:
            print("Course not found.")

    def handle_view_enrolled_courses_request(self):
        """
        Handles the request to view enrolled courses by calling the appropriate view method.
        """
        courses = self.student.view_enrolled_courses()
        self.view.render_enrolled_courses(courses)


# ==========================
# Main Application
# ==========================
if __name__ == "__main__":
    # Create some courses
    course1 = Course("C101", "Python Programming", 3)
    course2 = Course("C102", "Data Structures", 2)
    course3 = Course("C103", "Databases", 6)
    course4 = Course("C104", "Machine Learning", 5)

    # Create a student
    student_alice = Student(1, "Alice", "alice@hyperiondev.com")
    student_tom = Student(2, "Tom", "tom@hyperiondev.com")

    # Initialize the controller
    student_controller = StudentController(student_alice, [course1, course2, course3, course4])

    print("\nShow available courses...")
    student_controller.handle_show_available_courses_request()

    # Simulate student interactions
    print("\nEnrolling in a course...")
    student_controller.handle_enrollment_request()

    print("\nViewing enrolled courses...")
    student_controller.handle_view_enrolled_courses_request()

    print("\nEnrolling in another course...")
    student_controller.handle_enrollment_request()  # Enroll in Data Structures

    print("\nViewing enrolled courses...")
    student_controller.handle_view_enrolled_courses_request()

    print("\nDropping a course...")
    student_controller.handle_drop_request()  # Drop Python Programming

    print("\nViewing enrolled courses...")
    student_controller.handle_view_enrolled_courses_request()