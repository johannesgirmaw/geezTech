from applications.course.models import Course
from commons.utils.enums import PROGRESS_STATUS
from applications.chapters.serializers import ChapterSerializer
from applications.chapters.models import Chapter
from applications.content.models import Content
from rest_framework import generics
from applications.course_progress.models import UserChapterProgress, UserContentProgress, UserCourseProgress
from commons.utils.permissions import CustomPermission
from applications.course_progress.serializers import ChapterProgressSerializer, ContentProgressSerializer, CourseProgressSerializer


class CourseProgressDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [CustomPermission]
    queryset = UserCourseProgress.objects.all()
    serializer_class = CourseProgressSerializer


class CourseProgressListCreateView(generics.ListCreateAPIView):
    # permission_classes = [CustomPermission]
    queryset = UserCourseProgress.objects.all()
    serializer_class = CourseProgressSerializer


class ChapterProgressDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [CustomPermission]
    queryset = UserChapterProgress.objects.all()
    serializer_class = ChapterProgressSerializer


class ChapterProgressListCreateView(generics.ListCreateAPIView):
    # permission_classes = [CustomPermission]
    queryset = UserChapterProgress.objects.all()
    serializer_class = ChapterProgressSerializer


class ContentProgressListCreateView(generics.ListCreateAPIView):
    # permission_classes = [CustomPermission]
    queryset = UserContentProgress.objects.all()
    serializer_class = ContentProgressSerializer


class ContentProgressDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [CustomPermission]
    queryset = UserContentProgress.objects.all()
    serializer_class = ContentProgressSerializer

    # It should be based on requestee user
    def get_queryset(self):
        user = self.request.user
        data = UserContentProgress.objects.filter(user=user)
        return data

    def perform_update(self, serializer):

        # Check whether the content is last if not add next content
        content_progress_data = self.request.data

        current_content = Content.objects.get(
            id=content_progress_data["content"])

        last_content = Content.objects.filter(
            chapter=current_content.chapter).order_by("content_number").last()

        if current_content.id == last_content.id:

            # but if it is, update status to finished

            # check whether the chapter is the last chapter
            current_chapter = Chapter.objects.get(
                pk=current_content.chapter.id)

            last_chapter = Chapter.objects.filter(
                course=current_chapter.course).last()

            if current_chapter.id == last_chapter.id:
                chapter_progress = UserChapterProgress.objects.get(
                    chapter=last_chapter.id)

                chapter_progress.chapter_progress_status = PROGRESS_STATUS.FINISHED
                if serializer.is_valid():
                    serializer.save()
                    chapter_progress.save()

                # then update course to be finished
                current_course = Course.objects.get(
                    pk=current_chapter.course.id)
                current_course_progress_data = UserCourseProgress.objects.get(
                    course=current_chapter.course.id)

                if current_course.id == current_course_progress_data.course.id:
                    current_course_progress = UserCourseProgress.objects.get(
                        course=current_chapter.course.id)
                    current_course_progress.course_progress_status = PROGRESS_STATUS.FINISHED
                    current_course_progress.save()

            else:
                current_chapter_number = int(
                    current_chapter.chapter_number) + 1
                next_chapter_data = Chapter.objects.filter(
                    chapter_number=current_chapter_number).all()

                data = {"chapter": next_chapter_data.id,
                        "user": self.request.data['user'], "chapter_progress_status": PROGRESS_STATUS.STARTED}

                next_chapter_progress_serializer = ChapterProgressSerializer(
                    data=data)

                if next_chapter_progress_serializer.is_valid() and serializer.is_valid():
                    next_chapter_progress_serializer.save()
                    serializer.save()
                else:
                    print(
                        "------chapter progress or current content's serializer is invalid-------")
        else:

            current_content_number = int(current_content.content_number) + 1
            next_content_data = Content.objects.get(chapter=current_content.chapter,
                                                    content_number=current_content_number)

            # Add the next content
            data = {"content": next_content_data.id,
                    "user": self.request.data['user'], "content_progress_status": PROGRESS_STATUS.STARTED}
            next_content_progress_serializer = ContentProgressSerializer(
                data=data)
            # Update current content
            if next_content_progress_serializer.is_valid() and serializer.is_valid():
                next_content_progress_serializer.save()
                serializer.save()
            else:
                print(
                    "------next_content_progress_serializer or current content's serializer is invalid-------")
