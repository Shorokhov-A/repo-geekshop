from django.urls import path

from users.views import LoginFormView, RegistrationCreateView, ProfileUpdateView, logout

app_name = 'users'

urlpatterns = [
    path('login/', LoginFormView.as_view(), name='login'),
    path('registration/', RegistrationCreateView.as_view(), name='registration'),
    path('profile/<int:pk>/', ProfileUpdateView.as_view(), name='profile'),
    path('logout/', logout, name='logout'),
]
