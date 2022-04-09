from django.contrib import admin

from .models import Student, Subject, Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name")
    search_fields = ("full_name",)
    list_display_links = ("id", "full_name")
    ordering = ("full_name",)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
    list_display_links = ("id", "name")


class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "avg_grade")
    search_fields = ("full_name",)
    list_display_links = ("id", "full_name")
    ordering = ("full_name",)


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Student, StudentAdmin)
