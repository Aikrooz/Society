from django.urls import path
from .views import GroupView
urlpatterns=[
    path('group_creation/',GroupView.as_view(),name='group_creation')
]