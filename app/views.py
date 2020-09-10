from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def getImages(request):
    #http://127.0.0.1:8000/group/?imgCode=0c93885c4a1d416cac4386b6c5b85dae
    imgCode = request.GET['imgCode']
    imagepath = "D:/broadband_img/pic/20200805/" + imgCode + '.jpg'
    image_data = open(imagepath,"rb").read()
    return HttpResponse(image_data,content_type="image/png") #注意旧版的资料使用mimetype,现在已经改为content_type