import os


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


def mp4ToM3u8(src_path, new_path, name):

    ts_name = os.path.splitext(name)[0] + '.ts'
    m3u8_name = os.path.splitext(name)[0] + '.m3u8'


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


if __name__ == '__main__':
    #print(getResponseHeader("JPG"))

    mp4ToM3u8('X:/yy直播/','D:/web_application/nginx 1.7.11.3 Gryphon/html/','15012_1101280606_54880976_1598567424896.mp4')