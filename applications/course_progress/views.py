from rest_framework import generics
from applications.course_progress.models import UserChapterProgress, UserContentProgress, UserCourseProgress
from commons.permission.permissions import CustomPermission
from applications.course_progress.serializers import ChapterProgressSerializer, ContentProgressSerializer, CourseProgressSerializer


class CourseProgressDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    queryset = UserCourseProgress.objects.all()
    serializer_class = CourseProgressSerializer


class CourseProgressListCreateView(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    queryset = UserCourseProgress.objects.all()
    serializer_class = CourseProgressSerializer


class ChapterProgressDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    queryset = UserChapterProgress.objects.all()
    serializer_class = ChapterProgressSerializer


class ChapterProgressListCreateView(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    queryset = UserChapterProgress.objects.all()
    serializer_class = ChapterProgressSerializer


class ContentProgressListCreateView(generics.ListCreateAPIView):
    permission_classes = [CustomPermission]
    queryset = UserContentProgress.objects.all()
    serializer_class = ContentProgressSerializer


class ContentProgressDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermission]
    queryset = UserContentProgress.objects.all()
    serializer_class = ContentProgressSerializer
