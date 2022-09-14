import json
import os.path
import datetime
from django.shortcuts import render
from django.http.response import HttpResponse

cur_time = (datetime.datetime.now()).strftime("%Y-%m-%d").replace("-", "")

# Create your views here.
def Login(request):
    return HttpResponse('this is my first response!')

def AddData(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        file = './data.json'
        # if data is not None:
        print("data: ", data)
        # 对传入的数据进行存储
        json.dump(data, open(file, "w"))
        return HttpResponse(data)
    else:
        return HttpResponse('this is post url!')

def SetData(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        # if data is not None:
        # print("data: ", data)
        # data 是 json 格式，需要反解
        data = json.loads(data)
        # print('data.store: {}'.format(data["store"]))
        file = './{}_data.json'.format(data["store"])
        # cur_time_file = './{}_{}_data.json'.format(data["store"], cur_time)
        # print('data.product_sim: {}'.format(data["product_sim"]))
        # 对传入的数据进行存储
        json.dump(data, open(file, "w"))
        # os.system('cp file cur_time_file')
        return HttpResponse(data)
    else:
        return HttpResponse('this is post inferface!')


def GetData(request):
    if request.method == 'GET':
        store = request.GET.get('store')
        # print("store: {}".format(store))
        file = './{}_data.json'.format(store)
        data = {}
        if os.path.exists(file):
            with open(file, 'r') as load_f:
                data = json.load(load_f)
            # data = json.loads(file)
            # print("data: {}".format(data))
            # print('data.store: {}'.format(data["store"]))
            # print('data.product_sim: {}'.format(data["product_sim"]))
            datas = json.dumps({"Status": "success", "data": data})
            return HttpResponse(datas)
        else:
            return HttpResponse(json.dumps({"Status": "failed", "data": "NO DATA!"}))
    else:
        return HttpResponse('failed, this is get inferface!')


