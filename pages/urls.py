from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('book/<str:bookName>', views.bookDetail, name='bookdetail'),
    path('book/<str:bookName>/chapter<int:chapSeq>', views.chapDetail, name='chapDetail'),
]
