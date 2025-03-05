from courses.models import Category, Course, Lesson
from rest_framework import serializers

class BaseSeializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        d = super().to_representation(instance)
        d['image'] = instance.image.url
        return d
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class CourseSerializer(BaseSeializer):
    class Meta:
        model = Course
        fields= ['id', 'subject', 'description','image', 'created_date','category_id']

class LessonSerializer(BaseSeializer):
    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'created_date','image']
class LessonDetailSerializer(LessonSerializer):
    class Meta:
        model = LessonSerializer.Meta.model
        fields= LessonSerializer.Meta.fields + ['content', 'tag']