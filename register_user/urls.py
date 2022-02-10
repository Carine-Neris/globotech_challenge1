from django.urls import path,include
from .views import CreateUser,Employees,UpdateEmployees,home


urlpatterns = [
    path("registrar/", CreateUser.as_view(), name="register"),
    path("edit/employees/<int:pk>/",UpdateEmployees.as_view(),name="update"),
    path("list/employees", Employees.as_view(), name="list_employees"),
    path("", home, name="home"),
]

# Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls'), name="login"),
]