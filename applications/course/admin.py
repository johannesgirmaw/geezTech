from django.contrib import admin
from .models import Course

# Register your models here.


class CourseAdmin(admin.ModelAdmin):
    list_display = ('instructor_id', 'reviewer_id', 'course_name', 'course_code', 'course_image',
                    'course_description', 'course_video', 'course_price_id')


admin.site.register(Course, CourseAdmin)
