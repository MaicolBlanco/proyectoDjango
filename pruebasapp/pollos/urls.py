from nturl2path import url2pathname
from django.urls import path

from . import views

app_name = 'pollos'
urlpatterns = [
    # ex: /pollos/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /pollos/5/
    path('<int:pk>/detail/pruebas_para_validar',
         views.DetailView.as_view(), name='detail'),
    # ex: /pollos/5/results
    path('<int:pk>/results/',
         views.ResultView.as_view(), name='results'),
    # ex: /pollos/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
