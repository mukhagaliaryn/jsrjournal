from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('payment/', views.payment, name='payment'),
    path('article/', views.article, name='article'),
    path('create/', views.article_create, name='create'),
    path('pay/', views.article_payment, name='pay'),
    path('publishers/', views.publishers, name='publishers'),
    path('about/', views.about, name='about'),
    path('edit/task/', views.edit_task, name='edit_task'),
    path('edit/target/', views.edit_target, name='edit_target'),
    path('edit/compound/', views.edit_compound, name='edit_compound'),
]
