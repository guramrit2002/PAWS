from django.urls import path
from .views import PetRetreiveCreate,PetUpdateDeleteDetail
urlpatterns= [
    path('',PetRetreiveCreate.as_view(), name='pet'),
    path('<int:pk>',PetUpdateDeleteDetail.as_view(), name='retrieve')
]
