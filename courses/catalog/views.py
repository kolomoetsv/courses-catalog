from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, DeleteView, UpdateView

from .forms import CourseCreateForm
from .models import Course


# Create your views here.

def course_create(request):
    if request.method == "POST":
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.save()
            messages.add_message(request, messages.INFO, 'Курс успешно добавлен')
            return render(request, 'form-add-course.html')

    else:
        form = CourseCreateForm()
    return render(request, 'form-add-course.html', {'form': form})



class CourseListView(ListView):
    queryset = Course.objects.all()
    template_name = 'index.html'

    # Filters function
    def get_queryset(self):
        query = self.request.GET.get('q')
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        queryset = Course.objects.all()

        if query:
            queryset = queryset.filter(title__icontains=query)
        elif start_date:
            queryset = queryset.filter(start_date__gte=start_date)
        elif end_date:
            queryset = queryset.filter(end_date__lte=end_date)

        return queryset


class CourseDetailView(DetailView):
    queryset = Course.objects.all()
    template_name = 'course-detail.html'


class CourseDetailEdit(DetailView):
    queryset = Course.objects.all()
    template_name = 'course-detail.html'


# delete a course
class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'course-delete-confirm.html'
    success_url = '/'

    def get(self, *a, **kw):
        return self.delete(*a, **kw)


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'form-edit-course.html'
    fields = '__all__'

