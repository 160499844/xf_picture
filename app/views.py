from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from app.models import *
from django.shortcuts import redirect
import json
from django.http import HttpResponse
from app.utils import *
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf

def to_login_view(request):
    """登录页面"""
    return render(request, 'login.html', {})

def login_view(request):
    """登录"""
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/home')
    else:
        return render(request, 'login.html', {"msg":"用户名或者密码错误!"})


def logout_system(request):
    """退出登录"""
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/')
def getImages(request):
    """流加载图片"""
    #http://127.0.0.1:8000/group/?imgCode=0c93885c4a1d416cac4386b6c5b85dae
    imgCode = request.GET['imgCode']
    #imagepath = "D:/broadband_img/pic/20200805/" + imgCode + '.jpg'
    pic = PicItem.objects.get(id=imgCode)
    image_data = open(pic.resource,"rb").read()
    return HttpResponse(image_data,content_type=pic.res_header) #注意旧版的资料使用mimetype,现在已经改为content_type

@login_required(login_url='/')
def getPage(request):
    """获取文件夹中图片列表"""
    id = request.GET['id']
    page = request.GET['page']
    item = FolderItem.objects.get(id=id)
    images = PicItem.objects.filter(main=item)
    p = Paginator(images,24)
    rList = []
    page1 = p.page(page)
    for item in page1.object_list:
        resp = {'imgCode': item.id, 'imgName': item.file_name}
        rList.append(resp)
    page = {
        "content": rList,
        "count": p.num_pages
    }


    return HttpResponse(json.dumps(page), content_type="application/json")

@login_required(login_url='/')
def getPage(request):
    """获取文件夹中视频列表"""
    id = request.GET['id']
    page = request.GET['page']
    item = FolderItem.objects.get(id=id)
    images = PicItem.objects.filter(main=item)
    p = Paginator(images,24)
    rList = []
    page1 = p.page(page)
    for item in page1.object_list:
        resp = {'code': item.id, 'fileName': item.file_name}
        rList.append(resp)
    page = {
        "content": rList,
        "count": p.num_pages
    }


    return HttpResponse(json.dumps(page), content_type="application/json")

@login_required(login_url='/')
def update(request):
    """更新文件夹"""
    id = request.GET['id']
    item = FolderItem.objects.get(id=id)
    path  = os.walk(item.resource)
    #获取全部文件
    files = findAllFile(path)
    #删除全部
    PicItem.objects.filter(main=item).delete()
    #存到表中
    for imgItem in files:
        fpath, fname = os.path.split(imgItem)  # 分离文件名和路径
        p = PicItem()
        p.resource = imgItem
        p.type = fname.split(".")[-1]
        p.file_name = fname
        p.res_header = getResponseHeader(p.type)
        p.main = item
        p.save()
        print(imgItem)
    response = redirect('/static/html/end.html')
    return response

def getList(current_user):
    """获取全部文件夹"""

    tokens = UserToken.objects.filter(user=current_user)
    ids = []
    for item in tokens:
        ids.append(item.user.id)
    allItems = FolderItem.objects.filter(status='E').filter(folderItemFK__user_id__in=ids)
    print(allItems)
    return allItems
@login_required(login_url='/')
def getMyFolderItem(request):
    """获取全部文件夹"""
    current_user = request.user
    allItems = getList(current_user)

    return render(request, 'index.html', {"list":allItems})
@login_required(login_url='/')
def details(request):
    """获取文件夹中的文件"""
    id = request.GET['id']
    return render(request, 'details.html', {"id":id})
@login_required(login_url='/')
def play(request):
    id = request.GET['id']
    item = PicItem.objects.get(id=id)

    return render(request, 'play.html', {"movie":item})
@login_required(login_url='/')
def movies(request):
    """获取全部文件夹"""
    id = request.GET['id']
    return render(request, 'movies.html', {"id":id})
