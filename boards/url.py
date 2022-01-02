from boards import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('boards/<int:board_id>/', views.board_topics, name='board_topics'),
    path('boards/<int:board_id>/new', views.new_topic, name='new_topic'),
    path('api/topics/', views.topic_list, name='topics'),
    path('api/topics/detail/<int:pk>/', views.topic_detail, name='detail'),
    path('api/topics/create', views.topic_create, name='create'),
    path('api/topics/update/<int:pk>/', views.topic_update, name='update'),
    path('api/topics/delete/<int:pk>/', views.topic_delete, name='delete'),
]

