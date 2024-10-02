from django.urls import path, include
from . import views


app_name = 'MyUsers'

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('register/', views.Register, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
]