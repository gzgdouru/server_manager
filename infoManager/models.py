from django.db import models

# Create your models here.


class ServerInfo(models.Model):
    name = models.CharField(max_length=64, verbose_name="服务器名称", unique=True)
    host = models.CharField(max_length=128, verbose_name="服务器ip", unique=True)
    port = models.PositiveIntegerField(verbose_name="服务器端口")
    server_type = models.CharField(max_length=64, verbose_name="服务器类型")

    class Meta:
        db_table = "tb_server_info"

    def __str__(self):
        return self.host


class UserInfo(models.Model):
    server = models.ForeignKey(ServerInfo, on_delete=models.CASCADE, verbose_name="所属服务器")
    name = models.CharField(max_length=64, verbose_name="用户名")
    password = models.TextField(verbose_name="密码")

    class Meta:
        db_table = "tb_user_info"

    def __str__(self):
        return self.name