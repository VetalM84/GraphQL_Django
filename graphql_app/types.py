"""Object types for the GraphQL API."""

import graphene
from graphene_django import DjangoObjectType

from graphql_app.models import Student, Subject, Teacher


class TeacherType(DjangoObjectType):
    """Teacher object type."""

    class Meta:
        model = Teacher
        fields = ("id", "full_name", "subject")
        filter_fields = {
            "id": ["exact"],
            "full_name": ["exact", "icontains", "istartswith"],
        }
        interfaces = (graphene.relay.Node,)


class SubjectType(DjangoObjectType):
    """Subject object type."""

    class Meta:
        model = Subject
        fields = ("id", "name")
        filter_fields = {"name": ["exact", "icontains", "istartswith"]}
        interfaces = (graphene.relay.Node,)


class StudentType(DjangoObjectType):
    """Student object type."""

    class Meta:
        model = Student
        fields = ("id", "full_name", "avg_grade", "subject")
        filter_fields = {
            "id": ["exact"],
            "full_name": ["exact", "icontains", "istartswith"],
        }
        interfaces = (graphene.relay.Node,)
