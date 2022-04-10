import graphene
from django.contrib.auth import get_user_model
from graphql_jwt.shortcuts import create_refresh_token, get_token

from graphql_app.models import Student, Subject, Teacher
from graphql_app.types import StudentType, SubjectType, TeacherType


class TeacherInput(graphene.InputObjectType):
    id = graphene.ID()
    full_name = graphene.String()


class CreateTeacher(graphene.Mutation):
    class Arguments:
        # input = TeacherInput()
        full_name = graphene.String(required=True)
        id = graphene.ID()

    ok = graphene.Boolean()
    teacher = graphene.Field(TeacherType)

    @classmethod
    def mutate(cls, root, info, full_name, id=None):
        ok = True
        teacher_instance = Teacher.objects.create(full_name=full_name)
        return cls(ok=ok, teacher=teacher_instance)


class UpdateTeacher(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = TeacherInput(required=True)

    ok = graphene.Boolean()
    teacher = graphene.Field(TeacherType)

    @classmethod
    def mutate(cls, info, id, input=None):
        ok = False
        try:
            teacher_instance = Teacher.objects.get(pk=id)
        except Teacher.DoesNotExist:
            return cls(ok=ok, teacher=None)

        ok = True
        teacher_instance.full_name = input.full_name
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
