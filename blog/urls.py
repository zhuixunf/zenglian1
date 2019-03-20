from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:id>/', views.post_list, name='post_list'),
    path('post/create/', views.post_create, name='post_create'),
    path('post/delete/<int:id>/', views.post_delete, name='post_delete'),
    path('post/update/<int:id>/', views.post_update, name='post_update'),
]
