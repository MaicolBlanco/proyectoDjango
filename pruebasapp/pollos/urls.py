from nturl2path import url2pathname
from django.urls import path

from . import views

app_name = 'pollos'
urlpatterns = [
    # ex: /pollos/
    path('', views.index, name='index'),
    # ex: /pollos/5/
    path('<int:question_id>/detail/pruebas_para_validar',
         views.detail, name='detail'),
    # ex: /pollos/5/results
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /pollos/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
