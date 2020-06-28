from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator

from django.views import View
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from user.models import User
#三者全禁，可POST
# 'django.middleware.csrf.CsrfViewMiddleware',
# @csrf_protect  # 全局禁用csrf的情况 为某个视图单独添加csrf认证
# @csrf_exempt  # 为某个视图免除csrf认证
# 1.3. 开 可POST
# 1，'django.middleware.csrf.CsrfViewMiddleware',
# 2,@csrf_protect  # 全局禁用csrf的情况 为某个视图单独添加csrf认证
# 3,@csrf_exempt  # 为某个视图免除csrf认证
# 普通函数视图
def user(request):
    if request.method == "GET":
        print("GET SUCCESS  查询")
        return HttpResponse("GET SUCCESS")

    elif request.method == "POST":
        print("POST SUCCESS  添加")
        return HttpResponse("POST SUCCESS")

    elif request.method == "PUT":
        print("PUT SUCCESS  修改")
        return HttpResponse("PUT SUCCESS")

    elif request.method == "DELETE":
        print("DELETE SUCCESS  删除")
        return HttpResponse("DELETE SUCCESS")

# 让类视图免除csrf认证
@method_decorator(csrf_exempt, name="dispatch")
class UserView(View):
    #查询用户
    def get(self, request, *args, **kwargs):
        # 获取用户id
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

    # 新增单个用户
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

    #修改用户信息
    def put(self, request, *args, **kwargs):
        print("PUT SUCCESS  修改")
        return HttpResponse("PUT SUCCESS")

    #删除用户信息
    def delete(self, request, *args, **kwargs):
        # request:  WSGIrequest
        print("DELETE SUCCESS  删除")
        return HttpResponse("DELETE SUCCESS")


