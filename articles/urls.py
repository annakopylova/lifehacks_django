from django.urls import path

from . import views

urlpatterns = [
    # получение статьи
    path('<str:article_id>/', views.detail, name='detail'),
    # добавление статьи
    path('add', views.add_article, name='add'),
    path('map', views.get_map, name='map'),
    path('sections', views.get_sections, name='sections'),
    path('getallarticles', views.get_all_articles, name='allarticles'),
    path('addcomment', views.add_comment, name='allarticles'),
    path('getallcomments', views.get_all_comments, name='allarticles')
]