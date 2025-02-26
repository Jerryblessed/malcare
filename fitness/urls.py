from django.urls import path
from django.contrib.auth.views import LoginView
from .views import add_activity, add_diet_log, custom_logout, malcare_doc, profile
from . import views

# Define URL patterns
urlpatterns = [
    path('', views.home, name='home'),
    path('activities/', views.activity_list, name='activity_list'),
    path('diet/', views.diet_log, name='diet_log'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='fitness/login.html'), name='login'),
    path('malcare_doc/', malcare_doc, name='malcare_doc'),
    path('logout/', custom_logout, name='logout'),
    path('activities/add/', add_activity, name='add_activity'),
    path('diet/add/', add_diet_log, name='add_diet_log'),
    path('weight/', views.weight_tracker, name='weight_tracker'),
    path('profile/', profile, name='profile'),
]

# Custom error handlers (MUST be outside urlpatterns)
from django.conf.urls import handler404
from fitness.views import custom_404

handler404 = custom_404  # Assign the custom 404 handler
