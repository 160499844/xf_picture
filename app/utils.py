import os

#图片常用格式
endWiths = ['.jpg','.png','.gif','jpeg','bmp','webp','webp','tif']
#图片响应头
response_headers = {
    "jpg":"image/jpeg",
    "png":"image/png",
    "gif":"image/gif",
    "jpeg":"image/jpeg",
    "bmp":"image/bmp",
    "webp":"image/webp",
    "tif":"image/tif",
}

def getResponseHeader(item):
    item = item.lower()
    s = ""
    try:
        s = response_headers[item]
    except Exception as e:
        print(e)
    return  s


def findAllFile(base):
    """获取种文件"""
    list = []
    for path, d, filelist in base:

        for filename in filelist:
            filenameEnd = os.path.splitext(filename)[-1]
            if filenameEnd in endWiths:
                #print(os.path.join(path, filename))
                list.append(os.path.join(path, filename))

    return list
if __name__ == '__main__':
    print(getResponseHeader("JPG"))