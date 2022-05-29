import pandas as pd
from django.db import models


class Groups(models.Model):
    group_name = models.CharField(max_length=200, verbose_name = 'Группа')



'''class Groups(models.Model):
    file = pd.read_excel(r'src/groups/first.xls', sheet_name='поток И1')
    #print(file['ИДБ-21-02'].tolist())
    def __str__(self):
        return #self.text // если делаем текст переменную на поиск надо добавить перемен
'''

class Prepod(models.Model):
    poisk_name = models.CharField(max_length=200, verbose_name='Преподаватель')