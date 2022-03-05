from django.urls import path

from . import views

app_name = 'pollos'
urlpatterns = [
    # ex: /pollos/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /pollos/5/
    path('<int:pk>/detail/',
         views.DetailView.as_view(), name='detail'),
    # ex: /pollos/5/results
    path('<int:pk>/results/',
         views.ResultView.as_view(), name='results'),
    # ex: /pollos/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
