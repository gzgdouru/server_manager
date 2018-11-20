import json

from django.shortcuts import render
from django.views.generic import View
from django.core import serializers
from django.http import HttpResponse, JsonResponse

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from infoManager.models import ServerInfo, UserInfo
from infoManager.serializers import ServerInfoSerializer, UserInfoSerializer


# Create your views here.


class IndexView(View):
    def get(self, request):
        return render(request, "index.html", context={})


# class ServerInfoView(View):
#     def get(self, request):
#         servers = []
#         all_server = ServerInfo.objects.all()
#         for server in all_server:
#             servers.append({
#                 "id": server.id,
#                 "name": server.name,
#                 "host": server.host,
#                 "port": server.port,
#                 "server_type": server.server_type,
#             })
#         # data = serializers.serialize("json", servers)
#         return HttpResponse(json.dumps(servers), content_type="application/json")


# class UserInfoView(View):
#     def get(self, request):
#         server = request.GET.get("server")
#         if not server:
#             return JsonResponse({"msg":"请指定具体的服务器"})
#
#         username = request.GET.get("username")
#         if not username:
#             return JsonResponse({"msg": "请指定具有用户"})
#
#         server_obj = ServerInfo.objects.filter(pk=server).first()
#         if not server_obj:
#             return JsonResponse({"msg": "不存在的服务器({0})".format(server)})
#
#         user = UserInfo.objects.filter(server=server_obj, name=username).first()
#         if not user:
#             return JsonResponse({"msg": "该服务器({0})不存在用户({1})".format(server, username)})
#
#         data = {
#             "server_id": user.server.id,
#             "name": user.name,
#             "password": user.password,
#         }
#         return JsonResponse(data)


class ServerInfoView(ListAPIView):
    queryset = ServerInfo.objects.all()
    serializer_class = ServerInfoSerializer


class UserInfoView(APIView):
    def get(self, request):
        server = request.GET.get("server")
        if not server:
            return Response({"msg": "请指定具体的服务器(server=)"})

        username = request.GET.get("username")
        if not username:
            return Response({"msg": "请指定具有用户(username=)"})

        server_obj = ServerInfo.objects.filter(pk=server).first()
        if not server_obj:
            return Response({"msg": "不存在的服务器({0})".format(server)})

        user = UserInfo.objects.filter(server=server_obj, name=username).first()
        if not user:
            return Response({"msg": "该服务器({0})不存在用户({1})".format(server, username)})

        return Response({
            "server_id": user.server.id,
            "name": user.name,
            "password": user.password,
        })
