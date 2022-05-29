from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('groups/', groups, name='groups'),
    path('maps/', maps, name='maps'),
    path('useful/', useful, name='useful'),
    path('teachers/', teachers, name='teachers'),
    path('struct/', struct, name='struct'),
    path('schedule/', schedule, name='schedule'),
]