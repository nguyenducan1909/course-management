from courses.models import Category, Course, Lesson
from courses import serializers, paginators
from rest_framework import viewsets, generics

class CategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.filter(active = True)
    serializer_class = serializers.CategorySerializer


class CourseViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Course.objects.filter(active=True)
    serializer_class = serializers.CourseSerializer
    pagination_class = paginators.CoursePaginator


    def get_queryset(self):
        query = self.queryset

        q = self.request.query_params.get('q')
        if q:
            query = query.filter(subject__icontains=q)
        cate_id= self.request.query_params.get('category_id')
        if cate_id:
            query = query.filter(category_id=cate_id)
        return query
