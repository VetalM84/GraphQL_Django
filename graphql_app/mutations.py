import graphene
from django.contrib.auth import get_user_model
from graphql_jwt.shortcuts import create_refresh_token, get_token

from graphql_app.models import Student, Subject, Teacher
from graphql_app.types import StudentType, SubjectType, TeacherType


class TeacherInput(graphene.InputObjectType):
    full_name = graphene.String()
    subject = graphene.List(graphene.Int)
    id = graphene.ID()


class CreateTeacher(graphene.Mutation):
    class Arguments:
        input = TeacherInput(required=True)

    ok = graphene.Boolean()
    teacher = graphene.Field(TeacherType)

    @classmethod
    def mutate(cls, root, info, input=None):
        ok = True
        teacher_instance = Teacher.objects.create(full_name=input.full_name)
        teacher_instance.subject.add(*input.subject)
        return cls(ok=ok, teacher=teacher_instance)


class UpdateTeacher(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = TeacherInput(required=True)

    ok = graphene.Boolean()
    teacher = graphene.Field(TeacherType)

    @classmethod
    def mutate(cls, root, info, id, input=None):
        ok = False
        try:
            teacher_instance = Teacher.objects.get(pk=id)
        except Teacher.DoesNotExist:
            return cls(ok=ok, teacher=None)

        ok = True
        teacher_instance.full_name = input.full_name
        teacher_instance.subject.add(*input.subject)
        teacher_instance.save()
        return cls(ok=ok, teacher=teacher_instance)


class DeleteTeacher(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id):
        try:
            teacher_instance = Teacher.objects.get(pk=id)
            teacher_instance.delete()
            return cls(ok=True)
        except Teacher.DoesNotExist:
            return cls(ok=True)


class Mutation(graphene.ObjectType):
    create_teacher = CreateTeacher.Field()
    update_teacher = UpdateTeacher.Field()
    delete_teacher = DeleteTeacher.Field()
