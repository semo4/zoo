from django.urls import path
from . import views

app_name = 'Pets'
urlpatterns = [
    path('', views.home, name='home'),
    path('pets/', views.main, name='pets'),
    path('adoption_user/', views.adoption_user, name='adoption_user'),
    path('offer_adoption/', views.offer_adoption, name='offer_adoption'),
    path('pet_details/<int:pk>', views.pet_details, name='pet_details'),
    path('my_pets/', views.my_pets, name='my_pets'),
    path('apply_adoption/<int:pk>', views.apply_adoption, name='apply_adoption'),
    path('about/', views.about, name='about'),
]
