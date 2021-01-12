import os
import shutil

#图片常用格式
img_endWiths = ['.jpg', '.png', '.gif', 'jpeg', 'bmp', 'webp', 'webp', 'tif']
video_endWiths = ['.mp4', '.avi']
#图片响应头
response_headers = {
    "jpg":"image/jpeg",
    "png":"image/png",
    "gif":"image/gif",
    "jpeg":"image/jpeg",
    "bmp":"image/bmp",
    "webp":"image/webp",
    "tif":"image/tif",
    "mp4":"video/x-mpg",
    "avi":"video/avi",
}

def getResponseHeader(item):
    item = item.lower()
    s = ""
    try:
        s = response_headers[item]
    except Exception as e:
        print(e)
    return  s


def findAllFileImg(base):
    """获取图片文件"""
    list = []
    for path, d, filelist in base:

        for filename in filelist:
            filenameEnd = os.path.splitext(filename)[-1]
            if filenameEnd in img_endWiths:
                #print(os.path.join(path, filename))
                list.append(os.path.join(path, filename))

    return list

def findAllFileVideo(base):
    """获取视频文件"""
    list = []
    for path, d, filelist in base:

        for filename in filelist:
            filenameEnd = os.path.splitext(filename)[-1]
            if filenameEnd in video_endWiths:
                #print(os.path.join(path, filename))
                list.append(os.path.join(path, filename))

    return list


def mkdir(path):
    # 引入模块
    import os

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print(path + ' 创建成功')

        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False



def mp4ToM3u8(src_path, new_path, name):

    ts_name = os.path.splitext(name)[0] + '.ts'
    m3u8_name = os.path.splitext(name)[0] + '.m3u8'

    # 定义要创建的目录
    new_path = new_path + os.path.splitext(name)[0] + '/'
    # 调用函数
    mkdir(new_path)


    cmd = "ffmpeg -y -i \"%s\" -vcodec copy -acodec copy -vbsf h264_mp4toannexb \"%s\"" %(src_path + name, new_path + ts_name)
    print(cmd)
    f = os.popen(cmd, "r")
    d = f.read()  # 读文件
    print(d)

    file_m3u8 = ""
    c_file_ts = ""

    #切片
    cmd = "ffmpeg -i \"" + new_path + ts_name + "\" -c copy -map 0 -f segment -segment_list \"" + new_path + m3u8_name + "\" -segment_time 10 \"" + new_path + "/15s_%3d.ts\""
    print(cmd)
    f = os.popen(cmd, "r")
    d = f.read()  # 读文件
    print(d)


    #删除ts文件
    os.remove(new_path + ts_name)

if __name__ == '__main__':
    #print(getResponseHeader("JPG"))

    mp4ToM3u8('X:/yy直播/','D:/web_application/data/movies/','15012_1101280606_54880976_1598571903758.mp4')