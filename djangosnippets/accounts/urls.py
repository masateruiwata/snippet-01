from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.contrib.auth.forms import UserCreationForm
from .views import SignupView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(
        redirect_authenticated_user=True,
        template_name='accounts/login.html'
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]