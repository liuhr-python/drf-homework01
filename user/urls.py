
from django.urls import path

from user import views
urlpatterns = [
    path("user/", views.user),
   # Django 开发接口
    path("users/<str:id>/", views.UserView.as_view()),
]
