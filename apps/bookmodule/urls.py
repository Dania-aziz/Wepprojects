from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # هذا السطر مهم
    path('index2/<int:val1>/', views.index2),
    path('<int:bookId>/', views.viewbook),  # أضف هذا السطر

]