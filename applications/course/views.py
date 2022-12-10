from django.core.exceptions import ValidationError
from applications.content.serializer import ContentSerializer
from applications.content.models import Content
from applications.chapters.serializers import ChapterSerializer
from applications.course_progress.serializers import ChapterProgressSerializer, ContentProgressSerializer, CourseProgressSerializer

from commons.utils.permissions import CustomPermission
from rest_framework import generics
from .models import Course, Course_Cart, CoursePrice, Enrollement, Reviewer
from .serializers import CoursePriceSerializer, CourseReviewSerializer, CourseSerializer, CourseCartSerializer, EnrollementSerializer
from rest_framework import filters
from applications.course_progress.models import UserCourseProgress
from rest_framework import serializers
from applications.chapters.models import Chapter


class CourseListCreateView(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # pagination_class = CustomCursorPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['course_name']
    ordering_fields = ['course_name', 'course_description']

    def perform_create(self, serializer):
        print(self.request)
        return super().perform_create(serializer)


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseCartListCreateView(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    queryset = Course_Cart.objects.all()
    serializer_class = CourseCartSerializer


class CourseCartDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    queryset = Course_Cart.objects.all()
    serializer_class = CourseCartSerializer


class EnrollementListCreateView(generics.ListCreateAPIView):
    # permission_classes = [CustomPermission]
    queryset = Enrollement.objects.all()
    serializer_class = EnrollementSerializer

    def perform_create(self, serializer):
        # Validation for user and course should be unique

        previous_enrollement = Enrollement.objects.filter(
            user=self.request.POST.get("user"), course=self.request.POST.get("course"))
        enrollment_serializer = EnrollementSerializer(data=self.request.data)

        if previous_enrollement.exists():
            raise serializers.ValidationError(
                ('Course is already enrolled'))
        else:
            # creating course progress
            data = {
                "course": self.request.POST.get("course"), "user": self.request.POST.get("user")}
            course_progress_serializer = CourseProgressSerializer(
                data=data)

            # creating chapter progress
            # get chapters sorted with this specific course
            chapter = Chapter.objects.filter(course=self.request.POST.get(
                "course")).order_by("chapter_number").first()
            chapter_progress_data = {
                "chapter": chapter.id, "user": self.request.POST.get("user")}
            chapter_progress_serializer = ChapterProgressSerializer(
                data=chapter_progress_data)

            # get content sorted with this specific course
            content = Content.objects.filter(
                chapter_id=chapter.id).order_by("content_number").first()
            content_progress_data = {
                "content": content.id, "user": self.request.POST.get("user")}
            content_progress_serializer = ContentProgressSerializer(
                data=content_progress_data)

            if content_progress_serializer.is_valid() and chapter_progress_serializer.is_valid() and course_progress_serializer.is_valid() and enrollment_serializer.is_valid():
                enrollment_serializer.save()
                course_progress_serializer.save()
                chapter_progress_serializer.save()
                content_progress_serializer.save()


class EnrollementDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [CustomPermission]
    queryset = Enrollement.objects.all()
    serializer_class = EnrollementSerializer


class ReviewerListCreateView(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    queryset = Reviewer.objects.all()
    serializer_class = CourseReviewSerializer


class ReviewerDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    queryset = Reviewer.objects.all()
    serializer_class = CourseReviewSerializer


class CoursePriceListCreateView(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    queryset = CoursePrice.objects.all()
    serializer_class = CoursePriceSerializer


class CoursePriceDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    queryset = CoursePrice.objects.all()
    serializer_class = CoursePriceSerializer
