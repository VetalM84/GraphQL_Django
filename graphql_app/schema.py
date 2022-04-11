"""Schema for graphql_app Models for GraphQL API."""

import graphene
from graphene_django.filter import DjangoFilterConnectionField

from graphql_app.models import Student, Subject, Teacher
from graphql_app.types import StudentType, SubjectType, TeacherType


class TeacherConnection(graphene.relay.Connection):
    """Pagination and slicing for Teachers list."""

    class Meta:
        node = TeacherType


class StudentConnection(graphene.relay.Connection):
    """Pagination and slicing for Students list."""

    class Meta:
        node = StudentType


class SubjectConnection(graphene.relay.Connection):
    """Pagination and slicing for Subjects list."""

    class Meta:
        node = SubjectType


class Query(graphene.ObjectType):
    """Query for GraphQL API."""

    teacher = graphene.relay.Node.Field(TeacherType)
    teachers = DjangoFilterConnectionField(TeacherType)

    subject = graphene.relay.Node.Field(SubjectType)
    subjects = DjangoFilterConnectionField(SubjectType)

    student = graphene.relay.Node.Field(StudentType)
    students = DjangoFilterConnectionField(StudentType)

    # teacher = graphene.Field(TeacherType, id=graphene.Int())
    # subject = graphene.Field(SubjectType, id=graphene.Int())
    # student = graphene.Field(StudentType, id=graphene.Int())
    # teachers = graphene.List(TeacherType)
    # subjects = graphene.List(SubjectType)
    # students = graphene.List(StudentType)

    def resolve_teacher(self, info, **kwargs):
        """Resolve Teacher by id."""
        num = kwargs.get("id", None)
        try:
            return Teacher.objects.get(pk=num)
        except Teacher.DoesNotExist:
            return None

    def resolve_subject(self, info, **kwargs):
        """Resolve Subject by id."""
        num = kwargs.get("id", None)
        try:
            return Subject.objects.get(pk=num)
        except Subject.DoesNotExist:
            return None

    def resolve_student(self, info, **kwargs):
        """Resolve Student by id."""
        num = kwargs.get("id", None)
        try:
            return Student.objects.get(pk=num)
        except Student.DoesNotExist:
            return None

    def resolve_teachers(self, info, **kwargs):
        """Resolve Teachers list."""
        return Teacher.objects.all()

    def resolve_subjects(self, info, **kwargs):
        """Resolve Subjects list."""
        return Subject.objects.all()

    def resolve_students(self, info, **kwargs):
        """Resolve Students list."""
        return Student.objects.all()
