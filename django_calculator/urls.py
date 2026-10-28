"""
URL configuration for django_calculator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from calculator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addition/',views.Addition_View.as_view()),
    path('subtraction/',views.Subtraction_View.as_view()),
    path('multiplication/',views.Multiplication_View.as_view()),
    path('division/',views.Division_View.as_view()),
    path('modulus/',views.Modulus_View.as_view()),
    path('percentage/',views.Percentage_View.as_view()),
    path('bmi/',views.BMI_View.as_view()),
    path('age/',views.Age_Calculator_View.as_view()),
    path('simple-interest/',views.Interest_Calculator_View.as_view()),
    path('electricity-bill/',views.Electricity_Calculator_View.as_view())
]