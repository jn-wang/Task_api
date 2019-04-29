from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import HttpResponse
import uuid
from api import models
class AuthView(APIView):
    def post(self,request,*args,**kwargs):
        ret = {'code':1000}
        user = request.data.get('user')
        pwd = request.data.get('pwd')
        user_list = models.UserInfo.objects.filter(user=user,pwd=pwd)

        if not user_list:
            ret['code']=1001
            ret['error']='用户名或密码错误'
        else:
            uid = str(uuid.uuid4())
            # 更新或创建token
            print(user)
            print(uid)
            models.UserToken.objects.update_or_create(user_id=user_list[0].id,defaults={'token':uid})
            ret['token'] = uid
        return Response(ret)

class RegisteredView(APIView):
    def post(self,request,*args,**kwargs):
        ret = {'code': 1000}
        user = request.data.get('user')
        pwd = request.data.get('pwd')
        email = request.data.get('email')
        tel = request.data.get('tel')
        models.UserInfo.objects.create(user=user,pwd=pwd,email=email,tel=tel)
        return Response(ret)

