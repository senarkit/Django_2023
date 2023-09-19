from home import views
from django.urls import path,include

urlpatterns = [
    path('', views.home, name='home'),
    path('SGN/', views.SGN, name='SGN'),
    # path('SGN', views.SGN, name='SGN'),
    path('HASE/', views.HASE, name='HASE'),
    path('MSB/', views.MSB, name='MSB')
]