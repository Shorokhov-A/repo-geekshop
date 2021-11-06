from django.urls import path

from users.views import LoginFormView, RegistrationCreateView, ProfileUpdateView, logout, send_verify_message

app_name = 'users'

urlpatterns = [
    path('login/', LoginFormView.as_view(), name='login'),
    path('registration/', RegistrationCreateView.as_view(), name='registration'),
    path('profile/<int:pk>/', ProfileUpdateView.as_view(), name='profile'),
    path('logout/', logout, name='logout'),
    path('verify/<str:email>/<str:activation_key>', send_verify_message, name='verify'),
]
