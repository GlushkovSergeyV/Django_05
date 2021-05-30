from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseNotFound, HttpResponseForbidden, HttpResponseServerError


from vacancies.models import Company, Specialty, Vacancy


def main_view(request):
    context_dict = {
        'specialty': Specialty.objects.all(),
        'company': Company.objects.all(),
    }
    return render(request, 'index.html', context=context_dict)


def vacancies_list_view(request):
    context_dict = {
        'specialty': Specialty.objects.all(),
    }
    return render(request, 'vacancies.html', context=context_dict)


def vacancies_cat_view(request, category):
    context_dict = {
        'specialty': Specialty.objects.filter(code=category),
    }
    return render(request, 'vacancies.html', context=context_dict)
# if Specialty.objects.filter(code=category).count() == 0:
#    return HttpResponseBadRequest('Нет вакансий выбранной категории!')


def vacancy_view(request, id):
    try:
        context_dict = {
            'vacancy': Vacancy.objects.get(id=id),
        }
        return render(request, 'vacancy.html', context=context_dict)
    except Vacancy.DoesNotExist:
        return HttpResponseNotFound('Вакансия с указанным идентификатором не найдена!')




def company_view(request, id):
    try:
        context_dict = {
            'company': Company.objects.get(id=id),
        }
        return render(request, 'company.html', context=context_dict)
    except Company.DoesNotExist:
        return HttpResponseNotFound('Компания с указанным идентификатором не найдена!')


def custom_handler400(request, exception):
    return HttpResponseBadRequest('Неверный запрос!')


def custom_handler403(request, exception):
    return HttpResponseForbidden('Доступ запрещен!')


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ресурс не найден!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')
