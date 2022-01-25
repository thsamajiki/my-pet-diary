from django.urls import path, include
from . import views

app_name = 'freeboard'

urlpatterns = [
    path('', views.board, name='board'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/write/', views.write, name='write'),
    path('<int:feed_id>/modify/', views.modify, name='modify'),
    path('<int:feed_id>/delete/', views.delete, name='delete'),
]