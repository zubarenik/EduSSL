from django.urls import path
from .views import TeacherList, TeacherInfo

urlpatterns = [
    path('teachers/', TeacherList.as_view(), name='teachers'),
    path('teacher/<int:id>/', TeacherInfo.as_view(), name='teacher'),
]
