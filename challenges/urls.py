from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:challenge_id>/', views.details, name='detail'),
    path('<int:challenge_id>/solve', views.solve, name='solve'),
]
