from django.http import Http404
from django.urls import path

from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('login', views.login_process_view, name='login_process'),
    path('logout', views.logout_view, name='logout'),
    path('search', views.search, name='search'),
    path('search/list', views.searchlist, name='searchlist'),
    path('language/select', views.index, name='index'),
    path('language/<int:lang_id>/search', views.search_form, name='search_form'),
    path('word/<int:word_id>/', views.view_word, name='view_word'),
    path('word/<int:word_id>/like/<int:translation_id>', views.like_word, name='like_word'),
    path('view_translation/<int:word_id>/', views.view_the_whole_translation, name='view_the_whole_translation'),
]