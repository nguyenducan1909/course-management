from courses.models import Category, Course, Lesson
from courses import serializers
from rest_framework import viewsets, generics

class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.filter(active = True)
    serializer_class = serializers.CategorySerializer