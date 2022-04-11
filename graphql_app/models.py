from django.db import models


class Teacher(models.Model):
    """Teacher model."""

    full_name = models.CharField(max_length=70, verbose_name="Full name")
    subject = models.ManyToManyField(
        "Subject", related_name="teacher_subject", verbose_name="Subject"
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"
        ordering = ["full_name"]


class Subject(models.Model):
    """Subject model."""

    name = models.CharField(max_length=100, verbose_name="Subject name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"
        ordering = ["name"]


class Student(models.Model):
    """Student model."""

    full_name = models.CharField(max_length=70, verbose_name="Full name")
    subject = models.ManyToManyField(
        "Subject", related_name="student_subject", verbose_name="Subject"
    )
    avg_grade = models.FloatField(verbose_name="Average grade")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ["full_name"]
