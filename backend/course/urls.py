from django.urls import path
from .views import IndexProcessing, CourseProcessing, PaymentProcessing, PromoCodeProcessing

urlpatterns = [
    path('index/', IndexProcessing.as_view(), name='index'),
    path('course/<int:id>/', CourseProcessing.as_view(), name='course'),
    path('check_payment/<int:id>/', PaymentProcessing.as_view(), name='payment'),
    path('check_promocode/<int:id>/', PromoCodeProcessing.as_view(), name='promocode'),
]
