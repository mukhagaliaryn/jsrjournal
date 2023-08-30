from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('payment/', views.payment, name='payment'),
    path('article/', views.article, name='article'),
    path('publishers/', views.publishers, name='publishers'),
    path('about/', views.about, name='about'),
]
