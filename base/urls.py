from django.urls import path, include
from .views import authView, home, ask_question

urlpatterns = [
 path("", home, name="home"),
 path("signup/", authView, name="authView"),
 path("accounts/", include("django.contrib.auth.urls")),
 path("ask_question/", ask_question, name="ask_question"),
]
