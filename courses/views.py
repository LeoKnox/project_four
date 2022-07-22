from django.shortcuts import render
from django.views.genericlist import ListView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Course

class OwnerMixin(object):
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)
class OwnerEditMixin(object):
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
class OwerCourseMixin(OwnerMixin):
    model = Course
    fields = ['subject', 'title', 'slug', 'overview']
    success_url = reverse_lazy('manage_course_list')
class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    template_name = 'courses/manage/course/form.html'
class ManagecourseListView(OwnerCourseMixin, Listview):
    template_name = 'courses/manage/course/list.html'
class CourseCreateView(OwnerCourseEditMixin, CreateView):
    pass
class CourseUpdateview(OwnerCourseEditMixin, UpdateView):
    pass
class CourseDeleteView(OwnercourseMixin, Deleteview):
    template_name = 'courses/maange/course/delete.html'

class ManageCourseListView(ListView):
    model = Course
    template_name = 'courses/manage/course/list.html'
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)