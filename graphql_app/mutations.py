"""CRUD for the GraphQL API."""

import graphene

from graphql_app.models import Student, Subject, Teacher
from graphql_app.types import StudentType, SubjectType, TeacherType


class SubjectInput(graphene.InputObjectType):
    """List of arguments for the Subject model."""

    name = graphene.String()
    id = graphene.ID()


class CreateSubject(graphene.Mutation):
    """Create a new subject."""

    class Arguments:
        """Arguments for the CreateSubject mutation."""

        input = SubjectInput(required=True)

    ok = graphene.Boolean()
    subject = graphene.Field(SubjectType)

    @classmethod
    def mutate(cls, root, info, input=None):
        """Method to create a new subject."""
        ok = True
        subject_instance = Subject.objects.create(name=input.name)
        return cls(ok=ok, subject=subject_instance)


class UpdateSubject(graphene.Mutation):
    """Update a subject."""

    class Arguments:
        """Arguments for the UpdateSubject mutation."""

        id = graphene.Int(required=True)
        input = SubjectInput(required=True)

    ok = graphene.Boolean()
    subject = graphene.Field(SubjectType)

    @classmethod
    def mutate(cls, root, info, id, input=None):
        """Method to update a subject."""
        ok = False
        try:
            subject_instance = Subject.objects.get(pk=id)
        except Subject.DoesNotExist:
            return cls(ok=ok, subject=None)

        ok = True
        subject_instance.name = input.name
        return cls(ok=ok, subject=subject_instance)


class DeleteSubject(graphene.Mutation):
    """Delete a subject."""

    class Arguments:
        """Arguments for the DeleteSubject mutation."""

        id = graphene.Int(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id):
        """Method to delete a subject."""
        try:
            subject_instance = Subject.objects.get(pk=id)
            subject_instance.delete()
            return cls(ok=True)
        except Teacher.DoesNotExist:
            return cls(ok=True)


class StudentInput(graphene.InputObjectType):
    """List of arguments for the Student model."""

    full_name = graphene.String()
    subject = graphene.List(graphene.Int)
    avg_grade = graphene.Float()
    id = graphene.ID()


class CreateStudent(graphene.Mutation):
    """Create a new student."""

    class Arguments:
        """Arguments for the CreateStudent mutation."""

        input = StudentInput(required=True)

    ok = graphene.Boolean()
    student = graphene.Field(StudentType)

    @classmethod
    def mutate(cls, root, info, input=None):
        """Method to create a new student."""
        ok = True
        student_instance = Student.objects.create(
            full_name=input.full_name, avg_grade=input.avg_grade
        )
        student_instance.subject.add(*input.subject)
        return cls(ok=ok, student=student_instance)


class UpdateStudent(graphene.Mutation):
    """Update a student."""

    class Arguments:
        """Arguments for the UpdateStudent mutation."""

        id = graphene.Int(required=True)
        input = StudentInput(required=True)

    ok = graphene.Boolean()
    student = graphene.Field(StudentType)

    @classmethod
    def mutate(cls, root, info, id, input=None):
        """Method to update a student."""
        ok = False
        try:
            student_instance = Student.objects.get(pk=id)
        except Student.DoesNotExist:
            return cls(ok=ok, teacher=None)

        ok = True
        student_instance.full_name = input.full_name
        student_instance.avg_grade = input.avg_grade
        student_instance.subject.add(*input.subject)
        student_instance.save()
        return cls(ok=ok, student=student_instance)


class DeleteStudent(graphene.Mutation):
    """Delete a student."""

    class Arguments:
        """Arguments for the DeleteStudent mutation."""

        id = graphene.Int(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id):
        """Method to delete a student."""
        try:
            student_instance = Student.objects.get(pk=id)
            student_instance.delete()
            return cls(ok=True)
        except Student.DoesNotExist:
            return cls(ok=True)


class TeacherInput(graphene.InputObjectType):
    """List of arguments for the Teacher model."""

    full_name = graphene.String()
    subject = graphene.List(graphene.Int)
    id = graphene.ID()


class CreateTeacher(graphene.Mutation):
    """Create a new teacher."""

    class Arguments:
        """Arguments for the CreateTeacher mutation."""

        input = TeacherInput(required=True)

    ok = graphene.Boolean()
    teacher = graphene.Field(TeacherType)

    @classmethod
    def mutate(cls, root, info, input=None):
        """Method to create a new teacher."""
        ok = True
        teacher_instance = Teacher.objects.create(full_name=input.full_name)
        teacher_instance.subject.add(*input.subject)
        return cls(ok=ok, teacher=teacher_instance)


class UpdateTeacher(graphene.Mutation):
    """Update a teacher."""

    class Arguments:
        """Arguments for the UpdateTeacher mutation."""

        id = graphene.Int(required=True)
        input = TeacherInput(required=True)

    ok = graphene.Boolean()
    teacher = graphene.Field(TeacherType)

    @classmethod
    def mutate(cls, root, info, id, input=None):
        """Method to update a teacher."""
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
    """Delete a teacher."""

    class Arguments:
        """Arguments for the DeleteTeacher mutation."""

        id = graphene.Int(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id):
        """Method to delete a teacher."""
        try:
            teacher_instance = Teacher.objects.get(pk=id)
            teacher_instance.delete()
            return cls(ok=True)
        except Teacher.DoesNotExist:
            return cls(ok=True)


class Mutation(graphene.ObjectType):
    """Register mutations for creating, updating and deleting."""

    create_teacher = CreateTeacher.Field()
    update_teacher = UpdateTeacher.Field()
    delete_teacher = DeleteTeacher.Field()

    create_student = CreateStudent.Field()
    update_student = UpdateStudent.Field()
    delete_student = DeleteStudent.Field()

    create_subject = CreateSubject.Field()
    update_subject = UpdateSubject.Field()
    delete_subject = DeleteSubject.Field()
