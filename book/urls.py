from django.urls import path
from .views import *

urlpatterns = [
    path('', BookList.as_view()),
    path('create/', BookCreate.as_view()),
    path('<int:pk>/', BookDetail.as_view()),
]
