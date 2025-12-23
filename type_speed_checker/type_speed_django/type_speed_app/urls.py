from django.urls import path
from .views import home, test_page, result

urlpatterns = [
    path('', home, name='home'),          # HOME
    path('test/', test_page, name='test'),# NEXT TEST
    path('result/', result, name='result')
]
