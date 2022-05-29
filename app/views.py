import json
import pandas as pd

from requests import request, get, post
from django.shortcuts import render
from django.http import HttpResponse
import requests


from .models import Groups
from .forms import GroupsForm

def index(request):
    context = {
        'title' : 'Главная страница'
    }
    return render(request, template_name='app/index.html', context=context)

def groups(request):
    groups = Groups()
    form = GroupsForm()
    context = {
        'groups': groups,
        'form': form,
        'title': 'Списки групп'
    }
    if request.method == 'POST':
        sn = str(request.POST['group_name'])
        sn = sn.upper()
        if sn in ['ИДБ-21-01', 'ИДБ-21-05']:
            file = pd.read_excel(r'src/groups/groups.xlsx', sheet_name=sn)
            file = file.fillna('')
            print(type(file))
            file = file.values.tolist()

            context['data'] = file
            context['g_name'] = request.POST['group_name']
            context['g_name'] = context['g_name'].upper()

            return render(request, template_name='app/groups.html', context=context)

        else:
            print('no no')
            data = 'not_found'
            context['data'] = data
            return render(request, template_name='app/groups.html', context=context)
    return render(request, template_name='app/groups.html', context=context)

def maps(request):
    context = {
        'title': 'Карта аудиторий'
    }
    return render(request, template_name='app/maps.html', context=context)

def useful(request):
    context = {
        'title': 'Полезное'
    }
    return render(request, template_name='app/useful.html', context=context)

from .models import Prepod
from .forms import PrepopForm

def teachers(request):# поиск по преподу
    prepod = Prepod()
    form = PrepopForm()
    context = {
        'groups': prepod,
        'form': form,
        'title': 'Список преподавателей'
    }

    if request.method == 'POST':
        #print(request.POST['poisk_name'])
        sn = str(request.POST['poisk_name'])
        req = requests.get("https://rinh-api.kovalev.team/employee/surname/" + sn)
        items = json.loads(req.text)
        print(f'найдено {len(items)} преподавателей')
        if len(items) > 0:
            a = []
            for i in items:
                #print(i['id'])
                r = requests.get("https://rinh-api.kovalev.team/employee/dto/" + str(i['id']))
                u = json.loads(r.text)
                #print(u['id'])
                print(u)
                a.append([u['employee']['avatarUrl'], u['employee']['fullName'], u['position']['name'], u['department']['name'], u['employee']['email'], u['employee']['phone']])
            context['data'] = a
            print(context['data'])
            return render(request, 'app/teachers.html', context)
        else:
            print('no no no')
            data = 'not_found'
            context['data'] = data
            return render(request, 'app/teachers.html', context)

        return render(request, 'app/teachers.html', context)

    else:
        print('no no no')
        data = None
        context['data'] = data
        return render(request, 'app/teachers.html', context)

def struct(request):
    context = {
        'title': 'Структура'
    }
    return render(request, template_name='app/struct.html', context=context)


def schedule(request):
    context = {
        'title': 'Расписание'
    }
    return render(request, template_name='app/schedule.html', context=context)



