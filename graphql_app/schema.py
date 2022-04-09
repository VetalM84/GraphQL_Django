import graphene
from graphene_django import DjangoObjectType

from .models import Student, Subject, Teacher


class TeacherType(DjangoObjectType):
    class Meta:
        model = Teacher
        fields = ("id", "full_name", "subject")


class SubjectType(DjangoObjectType):
    class Meta:
        model = Subject
        fields = ("id", "name")


class StudentType(DjangoObjectType):
    class Meta:
        model = Student
        fields = ("id", "full_name", "subject")


class Query(graphene.ObjectType):
    teacher = graphene.Field(TeacherType, id=graphene.Int())
    subject = graphene.Field(SubjectType, id=graphene.Int())
    student = graphene.Field(StudentType, id=graphene.Int())

    teachers = graphene.List(TeacherType)
    subjects = graphene.List(SubjectType)
    students = graphene.List(StudentType)

    def resolve_teacher(self, info, **kwargs):
        num = kwargs.get("id", None)
        try:
            return Teacher.objects.get(pk=num)
        except Teacher.DoesNotExist:
            return None

    def resolve_subject(self, info, **kwargs):
        num = kwargs.get("id", None)
        try:
            return Subject.objects.get(pk=num)
        except Subject.DoesNotExist:
            return None

    def resolve_student(self, info, **kwargs):
        num = kwargs.get("id", None)
        try:
            return Student.objects.get(pk=num)
        except Student.DoesNotExist:
            return None

    def resolve_teachers(self, info):
        return Teacher.objects.all()

    def resolve_subjects(self, info):
        return Subject.objects.all()

    def resolve_students(self, info):
        return Student.objects.all()


schema = graphene.Schema(query=Query)
