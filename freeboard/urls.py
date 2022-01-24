from django.urls import path, include
from . import views

app_name = 'freeboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('post/create/', views.post_create, name='post_create'),
]