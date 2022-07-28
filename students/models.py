from django.db import models
from django.template.loader import render_to_string

students = models.ManyToManyField(User, related_name='courses_joined', blank=True)

class ItemBase(models.Model):
    def render(self):
        return render_to_string(
            f'courses/content{self._meta.mode_name}.html', {'item': self}
        )