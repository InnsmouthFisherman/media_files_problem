from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list'),
    path('detail/<pk>/', views.detail, name='detail' ),
    path('create/', views.create_article, name='create'),
]
