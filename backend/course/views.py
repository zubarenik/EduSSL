import json
from copy import deepcopy
from hashlib import sha256

import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Course, Lesson, Theme, Subscriber, PromoCode
from backend.emails import send_email
from backend.settings import API, PUBLIC_KEY, PRIVATE_KEY, API_EMAIL


def get_absolute_image_url(request, image):
    return 'https://' + request.get_host() + '/static' + image.url


class CourseProcessing(APIView):
    @staticmethod
    def get(request, id):
        context = dict()
        current_course = Course.objects.get(id=id)
        context['title'] = current_course.title
        context['description'] = current_course.description
        context['cost'] = current_course.cost
        context['date_started'] = current_course.date_started
        if current_course.image:
            context['image'] = get_absolute_image_url(request, current_course.image)
        context['category'] = [item.title for item in Category.objects.filter(courses=current_course.id)]
        jobs = current_course.jobs.all()
        context['jobs'] = [(item.title,
                            item.description,
                            get_absolute_image_url(request, item.image)  if item.image else None)
                           for item in jobs]
        goals = current_course.goals.all()
        context['goals'] = [(item.title,
                             item.description)
                            for item in goals]
        skills = current_course.skills.all()
        context['skills'] = [(item.title,
                              item.description)
                             for item in skills]
        reviews = current_course.reviews.all()
        context['reviews'] = [(item.title,
                               item.job,
                               item.text,
                               get_absolute_image_url(request, item.image)  if item.image else None)
                              for item in reviews]
        teachers = current_course.teachers.all()
        context['teachers'] = [(item.id,
                                item.title,
                                item.description,
                                get_absolute_image_url(request, item.image) if item.image else None)
                               for item in teachers]
        lessons = Lesson.objects.filter(course=current_course.id).order_by('pk')
        context['lessons'] = [{'id': item.id,
                               'title': item.title,
                               'themes': [{"id": theme.id,
                                           "title": theme.title,
                                           "text": theme.text} for theme in Theme.objects.filter(lesson=item.id)]}
                              for item in lessons]
        return Response(context)

    @staticmethod
    def _get_tinkoff_token(jsn):
        data = deepcopy(jsn)
        data['Password'] = PRIVATE_KEY
        data.pop('Receipt', None)
        data.pop('DATA', None)
        data_items = sorted(list(data.items()), key=lambda p: p[0])
        data_values = [str(value) for key, value in data_items]
        data_str = ''.join(data_values)
        return sha256(data_str.encode('utf-8')).hexdigest()

    @staticmethod
    def _signed(jsn):
        data = deepcopy(jsn)
        data['Token'] = CourseProcessing._get_tinkoff_token(jsn)
        return data

    @staticmethod
    def _init_bank_transaction(course, person, discount):
        cost = course.cost * (100 - discount)

        response = requests.post(
            'https://securepay.tinkoff.ru/v2/Init',
            json=CourseProcessing._signed({
                "TerminalKey": PUBLIC_KEY,
                "Amount": cost,
                "OrderId": "EDUSSL2021" + str(person.id),
                "Description": course.title,
                "NotificationURL" : API + '/check_payment/' + str(person.id) + '/',
                "DATA": {
                    "Email": person.email
                },
                "Receipt": {
                    "Email": person.email,
                    "EmailCompany": API_EMAIL,
                    "Taxation": "usn_income",
                    "Items": [
                        {
                            "Name": course.title,
                            "Price": cost,
                            "Quantity": 1,
                            "Amount": cost,
                            "PaymentMethod": "full_prepayment",
                            "PaymentObject": "service",
                            "Tax": "none",
                        }
                    ]
                }
            })
        )

        data = json.loads(response.text)
        assert data['ErrorCode'] == '0'
        return Response({
            'link': data['PaymentURL'],
            'person': person.id
        })

    @staticmethod
    def post(request, id):
        context = request.data
        current_course = Course.objects.get(id=id)

        persons = Subscriber.objects.filter(course__id=id, email=context['email'])
        if persons.exists():
            current_person = persons.first()
            current_person.name = context['name']
            current_person.number = context['number']
            current_person.save()
        else:
            new_person = Subscriber(name=context['name'], email=context['email'], number=context['number'], course=current_course)
            new_person.save()

        person = Subscriber.objects.filter(course__id=id, email=context['email']).first()
        if current_course.cost != 0:
            discount = 0
            if context['promocode'] != "null":
                discount = PromoCode.objects.get(slug=context['promocode']).discount

            return CourseProcessing._init_bank_transaction(current_course, person, discount)
        send_email(person.email, current_course)
        return Response(False)


class PaymentProcessing(APIView):
    @staticmethod
    def post(request, id):
        person = Subscriber.objects.get(id=id)
        course = person.course

        if request.data['Status'] in ('REJECTED', 'REFUNDED'):
            person.status = 1
        elif request.data['Status'] == 'CONFIRMED':
            person.status = 2
            send_email(person.email, course)
        person.save()
        return Response({'Message': 'OK'})

    @staticmethod
    def get(request, id):
        return Response({'status': Subscriber.objects.get(id=id).status})


class PromoCodeProcessing(APIView):
    @staticmethod
    def get(request, id):
        promocode = PromoCode.objects.filter(slug=request.GET['slug'])
        if promocode.exists():
            return Response({'slug': request.GET['slug']})

        promocode = Course.objects.get(id=id).promocodes
        if promocode.exists():
            return Response({'slug': promocode.first().slug})
        else:
            return Response(None)


class IndexProcessing(APIView):
    @staticmethod
    def get(request):
        context = dict()
        context['courses'] = list()
        courses = Course.objects.all()
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
        context['categories'] = list()
        categories = Category.objects.all()
        for category in categories:
            current_category = dict()
            current_category['id'] = category.id
            current_category['title'] = category.title
            current_category['description'] = category.description
            current_category['courses'] = [item.id for item in category.courses.all()]
            context['categories'].append(current_category)
        return Response(context)
