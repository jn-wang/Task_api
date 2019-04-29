from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import HttpResponse
# from rest_framework.versioning import URLPathVersioning
# from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer 已经进行全局配置
from api import models
from rest_framework.viewsets import GenericViewSet,ViewSetMixin
from api.serializers.task_serializers import TaskSerializer,TaskDetailSerializer
class TaskView(ViewSetMixin,APIView):
    def list(self,request,*args,**kwargs):
        # 课程列表接口
        ret = {'code': 1000, 'data': None}
        try:
            queryset = models.Task.objects.all()
            print(queryset)
            ser = TaskSerializer(instance=queryset,many=True)
            print(ser.data)
            ret['data'] = ser.data
        except:
            ret['code'] = 1001
            ret['error'] = '失败'
        return Response(ret)

    def retrieve(self,request,*args,**kwargs):
        # 课程详细接口
        ret = {'code': 1000, 'data': None}
        try:
            pk = kwargs.get('pk')
            obj = models.Task.objects.filter(id=pk).first()
            ser = TaskDetailSerializer(instance=obj, many=False)
            ret['data'] = ser.data
        except:
            ret['code'] = 1001
            ret['error'] = '失败'
        return Response(ret)