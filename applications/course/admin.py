from django.contrib import admin
from .models import Course

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_code', 'course_image',
                    'description', 'course_price')


admin.site.register(Course, CourseAdmin)
