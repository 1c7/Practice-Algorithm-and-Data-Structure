# coding=utf-8
# python 3

# 这个主要是测下又拍云怎么用
# 参照了官方的文档以及下面这篇文章
# http://segmentfault.com/a/1190000000460216


# 注意你需要先上又拍云注册个账号
# 创建个空间获得 空间名
# 创建个操作员获得 操作员的用户名和密码,才行



# 上传完文件之后用 FTP 登陆上去查看就行了

# 上传成功后, 通过网址访问:  
# http://haha1.b0.upaiyun.com/upyun-python-sdk/tac.png
# 图片空间名.网址/目录/图片名




import upyun

# ------------------ CONFIG ---------------------
BUCKETNAME = 'haha1'   # 图片空间名
USERNAME = 'haha1'     # 操作员用户名
PASSWORD = '###'  # 操作员密码 
# -----------------------------------------------


def run():
    up = upyun.UpYun(BUCKETNAME, USERNAME, PASSWORD, timeout=30,
                 endpoint=upyun.ED_AUTO)
    rootpath = '/upyun-python-sdk/'

    try:
        print "Uploading a new picture to upyun from a file"
        headers = {"x-gmkerl-rotate": "180"} #传入图片旋转参数
        with open('tree1.png', 'rb') as f:
            res = up.put(rootpath + 'tac.png', f,
                     checksum=False, headers=headers)
        print "OKED"

    except upyun.UpYunServiceException as se:
        print "failed\n"
        print "Except an UpYunServiceException ..."
        print "HTTP Status Code: " + str(se.status)
        print "Error Message:    " + se.msg + "\n"
        if se.err:
            print se.err
    except upyun.UpYunClientException as ce:
        print "failed\n"
        print "Except an UpYunClientException ..."
        print "Error Message: " + ce.msg + "\n"


if __name__ == '__main__':
    run()












