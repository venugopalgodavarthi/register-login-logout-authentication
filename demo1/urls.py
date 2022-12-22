from django.urls import path
from demo1 import views
app_name = 'demo1'

urlpatterns = [
    path('user/', views.userview, name='user'),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('login/', views.loginview, name='loginview'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.registeruserview, name='register'),
]
