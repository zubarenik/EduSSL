from rest_framework.generics import ListCreateAPIView
from rest_framework.serializers import ModelSerializer, ReadOnlyField, SerializerMethodField
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Teacher


def get_absolute_image_url(request, image):
    return 'https://' + request.get_host() + '/static' + image.url


class TeachersSerializers(ModelSerializer):
    id = ReadOnlyField()
    image = SerializerMethodField()

    class Meta:
        model = Teacher
        fields = ('id', 'title', 'description', 'image')

    def get_image(self, object):
        return get_absolute_image_url(self.context['request'], object.image)


class TeacherList(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeachersSerializers


class TeacherInfo(APIView):
    @staticmethod
    def get(request, id):
        context = dict()
        teacher = Teacher.objects.get(id=id)
        context['title'] = teacher.title
        context['description'] = teacher.description
        context['text'] = teacher.text
        if teacher.image:
            context['image'] = get_absolute_image_url(request, teacher.image)
        context['courses'] = list()
        courses = teacher.teachers.all()
        for course in courses:
            current_course = dict()
            current_course['id'] = course.id
            current_course['title'] = course.title
            current_course['description'] = course.description
            current_course['cost'] = course.cost
            current_course['capacity'] = course.capacity
            current_course['date_started'] = course.date_started
            if course.image:
                current_course['image'] = get_absolute_image_url(request, course.image)
            context['courses'].append(current_course)
        return Response(context)
