from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from .forms import UserCreationForm, UserChangeForm
from django.shortcuts import render


def home(request):
    return render(request, "home.html")


class CreateUser(generic.CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('home')


class UpdateEmployees(generic.UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = "edit.html"
    success_url = reverse_lazy('list_employees')


class Employees(generic.ListView):
    model = User
    template_name = "employees.html"
    paginate_by = 10

