import graphene
from graphene_django import DjangoObjectType

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

