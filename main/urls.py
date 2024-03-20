from django.urls import path
from . import views


urlpatterns = [
    path('', views.register, name='register'),  # Render signup page as landing page
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('password_recovery/', views.password_recovery, name='password_recovery'),
    # Other URL patterns...
]
