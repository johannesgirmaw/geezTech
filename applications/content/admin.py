from django.contrib import admin
from .models import Content

# Register your models here.


class ContentAdmin(admin.ModelAdmin):
    list_display = ('chapter_id', 'content_title',
                    'content_description', 'content_description', 'url', 'content_creator_id', 'content_type')


admin.site.register(Content, ContentAdmin)
