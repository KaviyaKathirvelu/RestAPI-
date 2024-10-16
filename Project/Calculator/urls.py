# calculator/urls.py
# calculator/urls.py
from django.urls import path
from .views import AddNumbersView, index

urlpatterns = [
    path('', index, name='index'),
    path('add/', AddNumbersView.as_view(), name='add_numbers'),
]