from django.shortcuts import render,redirect

# Create your views here.

from django.contrib.auth.decorators import login_required

from django.contrib import auth

def login(request):
    if  request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        user = auth.authenticate(username=user,password=pwd)
        if user:
            auth.login(request,user)
            return  redirect('/a1/')
    return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/login/')

from django.contrib.auth.models import User
def reg(request):
    if  request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        User.objects.create_user(username=user,password=pwd)
        return redirect('/login/')
    return render(request, 'reg.html')

def a1(request):
    with open('./data/时间序列逐年数据.csv', 'r', encoding='utf8') as f:
        reader = csv.reader(f)
        data_list = list(reader)
    city_list = ['北京', '上海', '广州', '成都', '沈阳']
    ddc = {}
    for i in data_list:
        if ddc.get(i[1]):
            ddc[i[1]].append(int(i[2]))
        else:
            ddc[i[1]] = [int(i[2])]
    print(ddc)
    return render(request, 'a1.html',{'times':city_list,'data':ddc})


import csv

def a2(request):
    with open('./data/不同季度逐年数据.csv', 'r', encoding='utf8') as f:
        reader = csv.reader(f)
        data_list = list(reader)
    city_list = ['北京', '上海', '广州', '成都', '沈阳']
    ddc = {}
    for i in data_list:
        if ddc.get(i[1]):
            ddc[i[1]].append(int(i[2]))
        else:
            ddc[i[1]] = [int(i[2])]
    print(ddc)
    return render(request, 'a2.html', {'times': city_list, 'data': ddc})


def a3(request):
    with open('./data/一年中各个月份变化.csv', 'r', encoding='utf8') as f:
        reader = csv.reader(f)
        data_list = list(reader)
    city_list = ['北京', '上海', '广州', '成都', '沈阳']
    ddc = {}
    for i in data_list:
        if ddc.get(i[1]):
            ddc[i[1]].append(int(i[2]))
        else:
            ddc[i[1]] = [int(i[2])]
    return render(request, 'a3.html', {'times': city_list, 'data': ddc})


def a4(request):
    with open('./data/一天中不同时段.csv', 'r', encoding='utf8') as f:
        reader = csv.reader(f)
        data_list = list(reader)
    city_list = ['北京', '上海', '广州', '成都', '沈阳']
    ddc = {}
    for i in data_list:
        if ddc.get(i[1]):
            ddc[i[1]].append(int(i[2]))
        else:
            ddc[i[1]] = [int(i[2])]
    return render(request, 'a4.html', {'times': city_list, 'data': ddc})


def a5(request):

    with open('./data/不同季度逐年数据.csv', 'r', encoding='utf8') as f:
        reader = csv.reader(f)
        data_list = list(reader)
    city_list = ['北京', '上海', '广州', '成都', '沈阳']
    ddc = {}
    for i in data_list:
        if ddc.get(i[1]):
            ddc[i[1]].append(int(i[2]))
        else:
            ddc[i[1]] = [i[1],int(i[2])]
    print(ddc)
    return render(request, 'a5.html', {'times': city_list, 'data': ddc})

def a6(request):
    with open('./data/与风向之间的关系.csv', 'r', encoding='utf8') as f:
        reader = csv.reader(f)
        data_list = list(reader)
    city_list = ['北京', '上海', '广州', '成都', '沈阳']
    ddc = {}
    print(data_list)
    for i in data_list:
        if ddc.get(i[1]):
            ddc[i[1]].append(int(i[2]))
        else:
            ddc[i[1]] = [i[1],int(i[2])]
    print(ddc)
    return render(request, 'a6.html', {'times': city_list, 'data': ddc})

def a7(request):
    city_list = ['北京', '上海', '广州', '成都', '沈阳']
    color_dic = {
        '北京':'#37A2DA','广州':'#e06343','上海': '#37a354','成都': '#b55dba','沈阳':'#b5bd48',
    }
    with open('./data/pm2.5与露点之间的关系.csv', 'r', encoding='utf8') as f:
        reader = csv.reader(f)
        data_list = list(reader)

    ddc = {}
    for i in data_list:
        i[0] = i[0].replace('\ufeff','')
        if ddc.get(i[0]):
            ddc[i[0]].append([float(i[1]),float(i[2])])
        else:
            ddc[i[0]] = [[float(i[1]),float(i[2])]]
    item_list = []
    for name , item in ddc.items():
        dd = {}
        dd['city'] = name
        dd['color'] = color_dic[name]
        dd['data'] = item[:1000]
        item_list.append(dd)

    print(item_list)

    return render(request, 'a7.html',{'times': city_list, 'data': item_list})
def a8(request):
    city_list = ['北京', '上海', '广州', '成都', '沈阳']
    color_dic = {
        '北京': '#37A2DA', '广州': '#e06343', '上海': '#37a354', '成都': '#b55dba', '沈阳': '#b5bd48',
    }
    with open('./data/pm2.5与相对湿度之间的关系.csv', 'r', encoding='utf8') as f:
        reader = csv.reader(f)
        data_list = list(reader)

    ddc = {}
    for i in data_list:
        i[0] = i[0].replace('\ufeff', '')
        if ddc.get(i[0]):
            ddc[i[0]].append([float(i[1]), float(i[2])])
        else:
            ddc[i[0]] = [[float(i[1]), float(i[2])]]
    item_list = []
    for name, item in ddc.items():
        dd = {}
        dd['city'] = name
        dd['color'] = color_dic[name]
        dd['data'] = item[:1000]
        item_list.append(dd)

    print(item_list)


    return render(request, 'a8.html', {'times': city_list, 'data': item_list})
def a9(request):
    city_list = ['北京', '上海', '广州', '成都', '沈阳']
    color_dic = {
        '北京': '#37A2DA', '广州': '#e06343', '上海': '#37a354', '成都': '#b55dba', '沈阳': '#b5bd48',
    }
    with open('./data/pm2.5与温度之间的关系.csv', 'r', encoding='utf8') as f:
        reader = csv.reader(f)
        data_list = list(reader)

    ddc = {}
    for i in data_list:
        i[0] = i[0].replace('\ufeff', '')
        if ddc.get(i[0]):
            ddc[i[0]].append([float(i[1]), float(i[2])])
        else:
            ddc[i[0]] = [[float(i[1]), float(i[2])]]
    item_list = []
    for name, item in ddc.items():
        dd = {}
        dd['city'] = name
        dd['color'] = color_dic[name]
        dd['data'] = item[:1000]
        item_list.append(dd)

    print(item_list)
    return render(request, 'a9.html', {'times': city_list, 'data': item_list})
def a10(request):
    city_list = ['北京', '上海', '广州', '成都', '沈阳']
    color_dic = {
        '北京': '#37A2DA', '广州': '#e06343', '上海': '#37a354', '成都': '#b55dba', '沈阳': '#b5bd48',
    }
    with open('./data/pm2.5与大气压之间的关系.csv', 'r', encoding='utf8') as f:
        reader = csv.reader(f)
        data_list = list(reader)

    ddc = {}
    for i in data_list:
        i[0] = i[0].replace('\ufeff', '')
        if ddc.get(i[0]):
            ddc[i[0]].append([float(i[1]), float(i[2])])
        else:
            ddc[i[0]] = [[float(i[1]), float(i[2])]]
    item_list = []
    for name, item in ddc.items():
        dd = {}
        dd['city'] = name
        dd['color'] = color_dic[name]
        dd['data'] = item[:1000]
        item_list.append(dd)

    print(item_list)
    return render(request, 'a10.html', {'times': city_list, 'data': item_list})