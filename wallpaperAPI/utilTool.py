import jpype
import ast
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
import json
import requests
from .models import Rank
import ast
from django.views import generic
from rest_framework import viewsets
from .serializers import RankSerializer
from rest_framework import mixins
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.renderers import JSONRenderer


class DealData:
    data = {}

    def getDealData(self, data):
        for k, v in data.items():
            data[k] = str(v)
        mapString = str(data)  # 将集合类型转换问String类型
        jvmPath = jpype.getDefaultJVMPath()  # 用来添加JAVA虚拟机命令行参数
        ext_classpath = 'wallpaperAPI/com/util.jar'  # 直接python调用ext_classpath = './com/util.jar',很奇怪的问题
        # ext_classpath = './com/util.jar'
        jvmArg = '-Djava.class.path=' + ext_classpath
        if not jpype.isJVMStarted():
            jpype.startJVM(jvmPath, jvmArg)
        netEngine = jpype.JPackage('com').NetEngine  # 获取java中的类
        signatur = (netEngine())  # 用java中的类创建对象
        param = signatur.getRequstparam(mapString)  # 获取经过处理后的data参数，增加了_time、_ak、_sign等参数
        result = ast.literal_eval(str(param))
        return result
        jpype.shutdownJVM()


'''
将相关的参数存入数据库，通过更改数据库参数来达到请求不同的目的
直接返回资源的网页
'''


class ReadOnlyOneObjectViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    def list(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        params = serializer.data

        host = params['address']
        list = []
        for k, v in params.items():
            if (k in ['id', 'active_status', 'address'] or v is None):
                list.append(k)
        for i in list:
            params.pop(i)
        util = DealData()
        p = util.getDealData(params)
        r = requests.get(host, params=p)
        result = r.json()
        return JsonResponse(result['data'], safe=False)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset)
        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj
