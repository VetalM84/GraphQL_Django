from django.contrib import admin

from .models import Student, Subject, Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name")
    search_fields = ("full_name",)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "avg_grade")


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Student, StudentAdmin)
