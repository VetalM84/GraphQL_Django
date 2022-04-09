import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from graphql_app.models import Student, Subject, Teacher


class TeacherType(DjangoObjectType):
    class Meta:
        model = Teacher
        fields = ("id", "full_name", "subject")
        filter_fields = {
            "id": ["exact"],
            "full_name": ["exact", "icontains", "istartswith"],
        }
        interfaces = (graphene.relay.Node,)


class SubjectType(DjangoObjectType):
    class Meta:
        model = Subject
        fields = ("id", "name")
        filter_fields = {"name": ["exact", "icontains", "istartswith"]}
        interfaces = (graphene.relay.Node,)


class StudentType(DjangoObjectType):
    class Meta:
        model = Student
        fields = ("id", "full_name", "subject")
        filter_fields = {
            "id": ["exact"],
            "full_name": ["exact", "icontains", "istartswith"],
        }
        interfaces = (graphene.relay.Node,)


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

    def resolve_teachers(self, info, **kwargs):
        return Teacher.objects.all()

    def resolve_subjects(self, info, **kwargs):
        return Subject.objects.all()

    def resolve_students(self, info, **kwargs):
        return Student.objects.all()


schema = graphene.Schema(query=Query)
