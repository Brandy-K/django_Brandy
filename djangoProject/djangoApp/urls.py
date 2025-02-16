from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login_without_session/', views.login_without_session, name='login_without_session'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_with_session, name='login'),  # Fixed: Point to the correct login view
]