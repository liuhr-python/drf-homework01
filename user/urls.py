
from django.urls import path

from user import views
urlpatterns = [
   #  path("user/", views.user),
   # # Django 开发接口
   #  path("users/", views.UserView.as_view()),  #查询全部
   #  path("users/<str:id>/", views.UserView.as_view()),
   #  # DRF 开发接口
    path("api_user/", views.UserAPIView.as_view()),
    path("api_user/<str:id>/", views.UserAPIView.as_view()),
]
