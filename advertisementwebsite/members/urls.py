from django.urls import path
from .views import UserRegisterView, UpdateProfile, CreateProfile, ShowProfile

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('<int:pk>/update_profile_page', UpdateProfile.as_view(), name="update_profile_page"),
    path('createprofile/', CreateProfile.as_view(), name="create_profile_page"),
    path('showprofile/<int:pk>', ShowProfile.as_view(), name="show_profile"),
]