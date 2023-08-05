from django.urls import path

from .views import (
    SignInView,
    SignUpView,
    ProfileView,
    ProfilePasswordView,

    signOut,
    profile_avatar
)


urlpatterns = [
    path("profile", ProfileView.as_view(), name="profile"),
    path("profile/avatar", profile_avatar, name="avatar"),
    path("profile/password", ProfilePasswordView.as_view(), name="password"),

    path("sign-in", SignInView.as_view(), name="login"),
    path("sign-up", SignUpView.as_view(), name="register"),
    path("sign-out", signOut)
]
