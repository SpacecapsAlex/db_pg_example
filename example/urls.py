from django.urls import path
from .views import home, accept

urlpatterns = [
    path('', home),
    path('accept/', accept),
]
