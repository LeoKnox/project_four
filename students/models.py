from django.db import models

students = models.ManyToManyField(User, related_name='courses_joined', blank=True)