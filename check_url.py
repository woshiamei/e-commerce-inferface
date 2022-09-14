# from urllib import request,parse

import requests
import json
import time

# 用户维度的

def set_vid_data():
    # datas = {}
    # for i in pro_list:
    #     datas[i[0]] = i[1].split(',')
    datas = {'1': ['2', '3', '4']}
    vid_data = json.dumps({"store": "unice", "vid": "123", "value": "1,2,4,6"})
    if vid_data:
        # host = '127.0.0.1'
        host = '192.168.1.150'
        url = 'http://{}:8000/cache_set/'.format(host)
        a = 0
        while a != 200:
            try:
                response = requests.post(url, data={"data": vid_data})
                a = response.status_code
            except Exception as e:
                time.sleep(1)
                print(e)
        print('{}----{}(success)'.format(len(datas), a))
        print('{}----{}(success)'.format(response.content, a))
        p_data = []
    else:
        print("no data to upload")


def get_vid_data():
    # datas = {}
    # for i in pro_list:
    #     datas[i[0]] = i[1].split(',')
    # datas = {'1': ['2', '3', '4']}
    # vid_data = json.dumps({"store": "unice", "vid": "123", "value": "1,2,4,6"})
    # if vid_data:
        # host = '127.0.0.1'
    host = '192.168.1.150'
    url = 'http://{}:8000/cache_get/'.format(host)
    a = 0
    while a != 200:
        try:
            # response = requests.post(url, data={"data": vid_data})
            response = requests.get(url, params={"store": 'unice', "vid": "123"})
            a = response.status_code
        except Exception as e:
            time.sleep(1)
            print(e)
    # print('{}----{}(success)'.format(len(datas), a))
    print('{}----{}(success)'.format(response.content, a))
    # p_data = []
    # else:
    #     print("no data to upload")

# set_vid_data()
# get_vid_data()

def get_unice_data():
    # respondse = request.urlopen("http://127.0.0.1:8000/get_sim_products")
    url = "http://219.157.255.228:8000/user_reco/get_user_top/?store=unice&cid=0000"
    # url = "http://www.baidu.com"
    respondse = requests.get(url)
    # respondse_data = respondse.read().decode('utf-8')
    # print(respondse_data)
    # print(respondse.status_code)
    i = 0
    while respondse.status_code != 200 and i < 10:
        respondse = requests.get(url)
        i += 1
    if respondse.status_code == 200:
        print("inferface is normal!")


def set_data():
    # datas = {}
    # for i in pro_list:
    #     datas[i[0]] = i[1].split(',')
    datas = {'1': ['2', '3', '4']}
    cos_data = json.dumps({"store": "unice", "product_sim": datas})
    if datas:
        # host = '127.0.0.1'
        host = '192.168.1.211'
        url = 'http://{}:8000/set_data/'.format(host)
        a = 0
        while a != 200:
            try:
                response = requests.post(url, data={"data": cos_data})
                a = response.status_code
            except Exception as e:
                time.sleep(1)
                print(e)
        print('{}----{}(success)'.format(len(datas), a))
        p_data = []
    else:
        print("no data to upload")

def get_data():
    # datas = {}
    # for i in pro_list:
    #     datas[i[0]] = i[1].split(',')
    # datas = {'1': ['2', '3', '4']}
    datas = {}
    url = 'http://{}:8000/get_data/'.format('127.0.0.1')

    a = 0
    while a != 200:
        try:
            response = requests.get(url, params={"store": 'unice'})
            a = response.status_code
        except Exception as e:
            time.sleep(1)
            print(e)
    print('{}----{}(success)'.format(response.content, a))
    datas = response.json()
    print(datas)
    print(type(datas))

get_unice_data()
# set_data()
# get_data()