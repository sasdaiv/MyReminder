from django.urls import path
from . import  views


urlpatterns = [
    path('', views.index, name = 'home'),
    path('<int:pk>',views.TaskDeleteView.as_view(), name = 'delete'),
    path('about', views.about, name = 'about'),
    path('create', views.create, name = 'create')
]