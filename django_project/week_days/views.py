from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def day_of_week(request, day):
    dct = {
        'monday': 'в понедельник я жалею себя',
        'tuesday': 'во вторник - глазею в пропасть',
        'wednesday': 'в среду решаю проблему мирового голода (никому не говорите)',
        'thursday': 'в четверг - зарядка',
        'friday': 'ужин с собой, нельзя снова его пропускать',
        'saturday': 'в субботу - борьба с презрением к себе',
        'sunday': 'в воскресенье - иду на рождество'
    }
    if day in dct:
        return HttpResponse(day, dct[day])
    return HttpResponseNotFound(f'Not found {day}')
