from django.contrib import admin
from django.utils.safestring import mark_safe

from courses.models import Category, Course, Lesson , Tag

class MyLessonAdmin(admin.ModelAdmin):
    list_display = ['id','subject','created_date','course_id']
    search_fields = ['subject', 'content']
    list_filter = ['id','created_date','subject']
    readonly_fields = ['image_view']

    def image_view(self, lesson):
        return mark_safe(f"<img src='/static/{lesson.image.name}' width='120' />")

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson, MyLessonAdmin)
admin.site.register(Tag)

