from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    LogoutView
)
from accounts.views import RegistrationView

urlpatterns = [
    path('register/',view=RegistrationView.as_view()),
    path('login/',view=LoginView.as_view(),name='login'),
    path('logout/',view=LogoutView.as_view(),name='logout'),
]