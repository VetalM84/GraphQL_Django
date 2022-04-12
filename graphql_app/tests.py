"""Test cases for the GraphQL API."""

import json

from graphene_django.utils.testing import GraphQLTestCase
from graphql_app.models import Teacher, Student, Subject


class TeacherTestCase(GraphQLTestCase):
    """Test cases for Teacher model."""

    def setUp(self):
        """Create test data."""
        self.teacher_1 = Teacher.objects.create(full_name='Teacher 1')
        self.teacher_2 = Teacher.objects.create(full_name='Teacher 2')
        self.subject_1 = Subject.objects.create(name='Subject 1')
        self.subject_2 = Subject.objects.create(name='Subject 2')
        self.teacher_1.subject.add(self.subject_1, self.subject_2)
        self.teacher_2.subject.add(self.subject_1)

    def test_resolve_teachers(self):
        """Test list of all teachers."""
        response = self.query(
            """
            query { teachers { edges { node { id fullName subject { edges { node { id name } } } } } } }            
            """,
        )
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)
        self.assertEqual(len(content['data']['teachers']['edges']), 2)

    def test_resolve_teachers_filter(self):
        """Test list of teachers with filter (first 2)."""
        response = self.query(
            """
            query { teachers (first: 2) { edges { node { id fullName subject { edges { node { id } } } } } } }            
            """,
        )
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)

    def test_resolve_teacher(self):
        """Test a single teacher by id."""
        response = self.query(
            """
            query teacher ($id: ID!) { 
                teacher (id: $id) { id fullName subject { edges { node { id } } } } 
                }
            """,
            op_name='teacher',
            variables={"id": 'VGVhY2hlclR5cGU6MQ=='},
        )
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)

    def test_create_teacher(self):
        """Test mutation to create teacher with subjects assigned."""
        response = self.query(
            """
            mutation CreateTeacherMutation {
              createTeacher(input: {fullName: "Test Create", subject: [1, 2]}) {
                ok teacher { id fullName subject { edges { node { id name } } } } }
            }
            """,
            op_name='CreateTeacherMutation',
        )
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)

    def test_delete_teacher(self):
        """Test mutation to delete teacher by id."""
        response = self.query(
            """
            mutation DeleteTeacherMutation { deleteTeacher(id: 1) { ok } }
            """,
            op_name='DeleteTeacherMutation',
        )
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)

    def test_update_teacher(self):
        """Test mutation to update a teacher by id."""
        response = self.query(
            """
            mutation UpdateTeacherMutation {
              updateTeacher(id: 1, input: {fullName: "From Test", subject: [1, 2]}) {
                ok teacher { id fullName subject { edges { node { id name } } } } }
            }
            """,
            op_name='UpdateTeacherMutation',
        )
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)


class StudentTestCase(GraphQLTestCase):
    """Test cases for Student model."""

    def setUp(self):
        """Create test data."""
        self.student_1 = Student.objects.create(full_name='Student 1', avg_grade=50.5)
        self.student_2 = Student.objects.create(full_name='Student 2', avg_grade=74.0)
        self.subject_1 = Subject.objects.create(name='Subject 1')
        self.subject_2 = Subject.objects.create(name='Subject 2')
        self.student_1.subject.add(self.subject_1, self.subject_2)
        self.student_2.subject.add(self.subject_1)

    def test_resolve_students(self):
        """Test list of all students."""
        response = self.query(
            """
            query { students { edges { node { id fullName avgGrade subject { edges { node { id name } } } } } } }            
            """,
        )
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)
        self.assertEqual(len(content['data']['students']['edges']), 2)

    def test_resolve_students_filter(self):
        """Test list of students with filter (first 2)."""
        response = self.query(
            """
            query { students (first: 2) { edges { node { id fullName avgGrade subject { edges { node { id } } } } } } }            
            """,
        )
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)

    def test_resolve_student(self):
        """Test a single student by id."""
        response = self.query(
            """
            query student ($id: ID!) { 
                student (id: $id) { id fullName avgGrade subject { edges { node { id } } } } 
                }
            """,
            op_name='student',
            variables={"id": 'U3R1ZGVudFR5cGU6MQ=='},
        )
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)

    def test_create_student(self):
        """Test mutation to create student with subjects assigned."""
        response = self.query(
            """
            mutation CreateStudentMutation {
              createStudent(input: {fullName: "Test Create", avgGrade: 55.5, subject: [1, 2]}) {
                ok student { id fullName avgGrade subject { edges { node { id name } } } } }
            }
            """,
            op_name='CreateStudentMutation',
        )
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)

    def test_delete_student(self):
        """Test mutation to delete student by id."""
        response = self.query(
            """
            mutation DeleteStudentMutation { deleteStudent(id: 1) { ok } }
            """,
            op_name='DeleteStudentMutation',
        )
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)

    def test_update_student(self):
        """Test mutation to update a student by id."""
        response = self.query(
            """
            mutation UpdateStudentMutation {
              updateStudent(id: 1, input: {fullName: "From Test" avgGrade: 100.0 subject: [1, 2]}) {
                ok student { id fullName avgGrade subject { edges { node { id name } } } } }
            }
            """,
            op_name='UpdateStudentMutation',
        )
        content = json.loads(response.content)
        print(content)
        self.assertResponseNoErrors(response)
