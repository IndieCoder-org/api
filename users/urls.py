from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('users/register', views.user_create),
    path('user/', views.user_details),
    path('users/<int:pk>', views.user_update),
]

urlpatterns = format_suffix_patterns(urlpatterns)
