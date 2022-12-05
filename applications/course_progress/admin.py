from django.contrib import admin
from .models import UserCourseProgress
# Register your models here.


class CourseProgressAdmin(admin.ModelAdmin):
    list_display = ('course', 'user', 'course_progress_status')


admin.site.register(UserCourseProgress, CourseProgressAdmin)
