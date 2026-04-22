from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.post_by_category, name='post_by_category'),
]