from django.forms import ModelForm
from .models import Groups

from .models import Prepod

class GroupsForm(ModelForm):
    class Meta:
        model = Groups
        fields = '__all__'

class PrepopForm(ModelForm):
    class Meta:
        model = Prepod
        fields = '__all__'