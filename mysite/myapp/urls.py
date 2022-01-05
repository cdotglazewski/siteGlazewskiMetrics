from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:book_id>', views.book_by_id, name='book_by_id'),
    path('team_wins/', views.team_wins, name='teamWins'),
    path('load_teams/', views.load_teams, name='load_teams'),
    path('team_statistics/<str:team_name>', views.team_statistics, name='team_statistics')
] 