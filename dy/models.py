from django.db import models

# Create your models here.
# UserModel单个对象转成json数据：
# 1.
# models.py文件里面Claass
# UserModel添加to_json方法
import json


def to_json(self):
    return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))


# 2.
# 业务层
# UserModel调用to_json()
# 方法
# user_model = UserModel(title='职位1', content='内容1')
# user_model.save()
# json_data = user_model.to_json()
# return HttpResponse(json_data, content_type="application/json")
#
# # UserModel集合转成json数据：
# from django.core import serializers
#
#
# def find(request):
#     user__model_list = UserModel.objects.all()
#     json_data = serializers.serialize('json', user__model_list)
#     return HttpResponse(json_data, content_type="application/json")
