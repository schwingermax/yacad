from django.urls import path
from . import views

urlpatterns = [
    path('continent/', views.continent_list),
    path('continent/<int:pk>', views.continent_detail),
]

1