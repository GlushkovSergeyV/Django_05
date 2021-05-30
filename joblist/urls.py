"""joblist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
#from django.contrib import admin
from django.urls import path
from vacancies.views import custom_handler400, custom_handler403, custom_handler404, custom_handler500
import vacancies.views as vacancies_views


urlpatterns = [
    path('', vacancies_views.main_view, name='main'),
    path('vacancies/', vacancies_views.vacancies_list_view, name='vacancy_all'),
    path('vacancies/cat/<str:category>', vacancies_views.vacancies_cat_view, name='vac_by_cat'),
    path('vacancies/<int:id>/', vacancies_views.vacancy_view, name='vac_by_id'),
    path('companies/<int:id>/', vacancies_views.company_view, name='companies'),
]

handler400 = custom_handler400
handler403 = custom_handler403
handler404 = custom_handler404
handler500 = custom_handler500
