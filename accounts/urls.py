# File location: D:\Placement_Prep\brainlyBeam\Task 2\jwt_auth\accounts\urls.py

from django.urls import path
from .views import SignupView  # Import the SignupView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
]
