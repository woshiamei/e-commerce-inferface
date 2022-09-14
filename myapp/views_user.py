import json
import os.path
import datetime
from django.shortcuts import render
from django.http.response import HttpResponse
from django.core.cache import cache

cur_time = (datetime.datetime.now()).strftime("%Y-%m-%d").replace("-", "")


# Create your views here.
def CacheTest(request):
	# 保存数据
	cache.set('uid', '123', 120)
	# 获取数据
	uid = cache.get('uid')
	print("缓存中 uid 为： ", uid)
	return HttpResponse('this is a cache test!')

expired_time = 90 * 24 * 3600

def SetUserTop(request):
	if request.method == 'POST':
		datas = request.POST.get('data')
		datas = json.loads(datas)
		for data in datas:
			store = data['store']
			# print("store: {}".format(store))
			# vid = data['vid']
			cid = data['cid']
			top_list = data['top_list']
			key = store + '_' + str(cid)
			cache.set(key, top_list, expired_time)
			value = cache.get(key)
			# print("res: {}".format([key, value]))
		return HttpResponse(json.dumps({"Status": "success", "data_num": len(datas)}))
	else:
		return HttpResponse('failed, this is post inferface!')

def GetUserTop(request):
	if request.method == 'GET':
		store = request.GET.get('store')
		cid = request.GET.get('cid')
		key = store + '_' + str(cid)
		try:
			value = cache.get(key)
		except:
			value = ""
			# print("no key: {}".format(key))
		# 未访问到的用户使用默认数据填充
		if value is None:
			print("cache miss!")
			key_default = store + '_' + '0000'
			value = cache.get(key_default)
		# 	return HttpResponse(json.dumps({"Status": "success", "data": [key, value]}))
		return HttpResponse(json.dumps({"Status": "success", "data": [key, value]}))
	else:
		return HttpResponse('failed, this is get inferface!')

def CacheSet(request):
	if request.method == 'POST':
		data = request.POST.get('data')
		# data 是 json 格式，需要反解
		data = json.loads(data)
		store = data['store']
		print("store: {}".format(store))
		vid = data['vid']
		value = data['value']
		key = store + '_' + vid
		cache.set(key, value, expired_time)
		value = cache.get(key)
		print("res: {}".format([key, value]))
		return HttpResponse(json.dumps({"Status": "success", "data": [key, value]}))
	else:
		return HttpResponse('failed, this is post inferface!')


def CacheGet(request):
	if request.method == 'GET':
		store = request.GET.get('store')
		vid = request.GET.get('vid')
		key = store + '_' + vid
		value = cache.get(key)
		if value is None:
			print("key: {}, value: {}".format(key, value))
			return HttpResponse(json.dumps({"Status": "None", "data": [key, value]}))
		else:
			print("key: {}, value: {}".format(key, value))
			return HttpResponse(json.dumps({"Status": "success", "data": [key, value]}))
	else:
		return HttpResponse('failed, this is get inferface!')