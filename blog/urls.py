import blog.views as views
from django.urls import path

urlpatterns = [
    path('create/', views.create, name='create'),
]