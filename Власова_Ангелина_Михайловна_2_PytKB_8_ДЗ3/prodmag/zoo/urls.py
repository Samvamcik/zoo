from django.contib import admin
from django.urls import path
from core.views import animals_view, animal_view

urlpatterns = [
    path('admin/',admin.site.urls),
    path('animals/', animals_view, name = 'animal'),
    path('animals/<int:id>', animal_view, name = 'animal')
]