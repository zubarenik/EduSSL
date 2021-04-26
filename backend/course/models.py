from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    courses = models.ManyToManyField('course.Course', related_name='courses', blank=True)


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    email_text = models.TextField(default="", blank=True, null=True)
    cost = models.IntegerField()
    capacity = models.IntegerField()
    date_started = models.CharField(max_length=20)
    image = models.ImageField(upload_to='course', blank=True, null=True, default=None)
    jobs = models.ManyToManyField('course.Job', related_name='jobs', blank=True)
    goals = models.ManyToManyField('course.Goal', related_name='goals', blank=True)
    skills = models.ManyToManyField('course.Skill', related_name='skills', blank=True)
    teachers = models.ManyToManyField('teacher.Teacher', related_name='teachers', blank=True)
    reviews = models.ManyToManyField('course.Review', related_name='reviews', blank=True)
    promocodes = models.ManyToManyField('course.PromoCode', related_name='promocodes', blank=True)


class PromoCode(models.Model):
    slug = models.CharField(max_length=40)
    discount = models.PositiveIntegerField()


class Lesson(models.Model):
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    text = models.TextField()


class Theme(models.Model):
    lesson = models.ForeignKey('course.Lesson', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    text = models.TextField()


class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='job', blank=True, null=True, default=None)


class Goal(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)


class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)


class Review(models.Model):
    title = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='review', blank=True, null=True, default=None)


class Subscriber(models.Model):
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=30)
    status = models.IntegerField(default=0, blank=True, null=True)
