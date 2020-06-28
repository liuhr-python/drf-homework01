from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator

from django.views import View
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from rest_framework.views import APIView
from rest_framework.response import Response

from user.models import User


class UserAPIView(APIView):

    # 获取用户信息
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get("id")
        if user_id:  # 查询单个
            user_val = User.objects.filter(pk=user_id).values("username", "password", "gender").first()
            if user_val:
                # 查询出对应用户信息，将用户信息返回到前端
                return JsonResponse({
                    "status": 200,
                    "message": "查询单体用户成功",
                    "results": user_val
                })
        else:
            # 没有传参数id  查询全部
            user_list = User.objects.all().values("username", "password", "gender")
            print(type(user_list))
            if user_list:
                return JsonResponse({
                    "status": 200,
                    "message": "查询全部用户成功",
                    "results": list(user_list),
                })

        return JsonResponse({
            "status": 500,
            "message": "查询失败",
        })

    # 添加用户信息
    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        try:
            user_obj = User.objects.create(username=username, password=pwd)
            return JsonResponse({
                "status": 201,
                "message": "创建用户成功",
                "results": {"username": user_obj.username, "gender": user_obj.gender}
            })
        except:
            return JsonResponse({
                "status": 500,
                "message": "创建用户失败",
            })
