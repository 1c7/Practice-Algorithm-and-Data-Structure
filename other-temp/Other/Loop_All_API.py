'''

Date  : 2015-12-11
Author: Cheng
程序说明: 这个程序用于测试 iOS 提供的接口列表地址
程序会逐个访问接口, 把不能访问的(404)记录下来


本程序的开发环境是 Ubuntu + Python3
用了一个第三方库 requests
可以用 pip3 install requests 安装

执行方法: 在命令行输入 python3 TOHO_Test_All_API.py

'''

import re
import requests
import sys
import json
import time


# 错误日志的存放文件名
fp = open("TOHO_API_Error_Log.txt", 'a')
current_time = time.strftime('%Y-%m-%d %H:%M:%S')
fp.write('测试时间: ')
fp.write(current_time)
fp.write('\n')


# 请修改如下字符串
string = '''
/**     登录注册的API      **/
/** 注册 */
#define RegisterURL @"http://tophot.host.smartgslb.com/?m=api&c=member&a=signup"
/** 登录 */
#define LoginURL @"http://tophot.host.smartgslb.com/?m=api&c=member&a=login"
/** 第三方登录 */
#define LoginThirdPartURL @"http://tophot.host.smartgslb.com/?m=api&c=member&a=thirdPartLogin"
/** 忘记密码 */
#define ForgetPWDURL @"http://tophot.host.smartgslb.com/?m=api&c=member&a=signup&action=forget"
/** 验证用户登录状态,可能没有登录过,可能登陆过但是已经失效了,做一个记录,在程序中的某些地方可能用到 */
#define CheckUserState @"http://tophot.host.smartgslb.com/?m=api&c=member&a=verify_token"


/**     我的API      **/
/** 上传头像 */
#define UploadHeaderImage @"http://tophot.host.smartgslb.com/?m=api&c=member&a=change_portrait"
#define UPloadTest @"http://tophot.host.smartgslb.com/?m=api&c=member&a=iOSFileUpload"
/** 获取用户信息 */
#define GetUserInfo @"http://tophot.host.smartgslb.com/?m=api&c=member&a=getInfo"
/** 更新用户信息 */
#define UploadUserInfo @"http://tophot.host.smartgslb.com/?m=api&c=member&a=TH_change_info"
/** 获取用户积分 */
#define GetUserTotalScore @"http://tophot.host.smartgslb.com/?m=api&c=member&a=get_user_score"
/** 获取积分列表 */
#define GetScoreList @"http://tophot.host.smartgslb.com/?m=api&c=member&a=get_score_list"
/** 上传用户建议 */
#define UploadSuggestion @"http://tophot.host.smartgslb.com/?m=api&c=feedback&a=submit"
/** 获取用户加入教练进程的状态 */
#define GetCoachState @"http://tophot.host.smartgslb.com/?m=api&c=cocach&a=status"
/** 上传教练信息详情 */
#define UploadCoachDetailMessages @"http://tophot.host.smartgslb.com/?m=api&c=cocach&a=join"
/** 获取我的积分明细 */
#define GetMyGetScoreDetail @"http://tophot.host.smartgslb.com/?m=api&c=member&a=get_score_detail"
/** 获取我的收藏 / 我的发布(c=collect这个参数标识),
 还有一个参数,用来标识是获取日记/日记本/咨询收藏 (a=diary)*/
#define GetMyCollectionOrMyPublish @"http://tophot.host.smartgslb.com/?m=api"
/** 获取我的礼券 */
#define GetMyGiftVouchers @"http://tophot.host.smartgslb.com/?m=api&c=coupons&a=myCoupons"
/** 绑定我的手机号 / 修改手机号 */
#define RelatedOrChangePhone @"http://tophot.host.smartgslb.com/?m=api&c=order&a=changePhoneNumber"
/** 我的发布/收到的评论,用a 参数标识 (a=receive,标识我收到的,a=comment标识我发布的评论) */
#define GetMyPublishOrReceiveComment @"http://tophot.host.smartgslb.com/?m=api&c=my"



/**     首页的API      **/
/** 获取首页帖子信息 */
#define GetHomeShows @"http://tophot.host.smartgslb.com/?m=api&c=index&a=index"



/**     圈子的API      **/
/** 获取圈子第一页帖子信息,有日记贴和问答贴 */
#define GetCircleShows @"http://tophot.host.smartgslb.com/?m=api&c=group&a=index"
/** 获取圈子 --精选日记贴 */
#define GetEssenceDiaryShows @"http://tophot.host.smartgslb.com/?m=api&c=diary&a=best_post"
/** 获取圈子 --日记贴 -- 日记本*/
#define GetNotebookMessage @"http://tophot.host.smartgslb.com/?m=api&c=diary&a=blog"
/** 获取圈子 --日记贴 -- 日记本 -- 日记详情页面*/
#define GetDiaryDetial @"http://tophot.host.smartgslb.com/?m=api&c=diary&a=article"
/** 获取圈子 --日记贴 -- 收藏 */
#define collectedDiary @"http://tophot.host.smartgslb.com/?m=api&c=diary&a=articleCollect"
/** 日记本的收藏 */
#define CollectedNotebook @"http://tophot.host.smartgslb.com/?m=api&c=diary&a=blogCollect"
/** 获取圈子 --日记贴 -- 喜欢 */
#define LikeDiary @"http://tophot.host.smartgslb.com/?m=api&c=diary&a=articleLike"
/** 获取圈子 --问答贴 */
#define GetEssenceConsultShows @"http://tophot.host.smartgslb.com/?m=api&c=question&a=bestQuestion"
/** 获取圈子 --问答贴 -- 问答详情页面 */
#define GetConsultDetail @"http://tophot.host.smartgslb.com/?m=api&c=question&a=detail"
/** 获取圈子 --问答贴 -- 收藏 */
#define collectedConsult @"http://tophot.host.smartgslb.com/?m=api&c=question&a=collect"
/** 获取圈子 --问答贴 -- 喜欢 */
#define LikeConsult @"http://tophot.host.smartgslb.com/?m=api&c=question&a=questionLike"
/** 获取圈子 --日记贴 -- 发表评论 */
#define PublishDiaryComment @"http://tophot.host.smartgslb.com/?m=api&c=diary&a=articleComment"
/** 获取圈子 --问答贴 -- 发表评论 */
#define PublishConsultComment @"http://tophot.host.smartgslb.com/?m=api&c=question&a=createComment"
/** 问答贴评论喜欢 */
#define LikeConsultComment @"http://tophot.host.smartgslb.com/?m=api&c=question&a=commentsLike"
/** 日记贴的评论喜欢 */
#define LikeDiaryComment @"http://tophot.host.smartgslb.com/?m=api&c=diary&a=articleCommentLike"


/**     福利的API      **/
/** 获取福利第一页数据 */
#define GetWelfares @"http://tophot.host.smartgslb.com/?m=api&c=product&a=home"
/** 获取教练详情 */
#define GetCoachDetail @"http://tophot.host.smartgslb.com/?m=api&c=cocach&a=home"
/** 获取用户的优惠券和积分详情 */
#define GetCouponAndScore @"http://tophot.host.smartgslb.com/?m=api&c=order&a=getCouponAndScore"
/** 获取服务器生成的的订单id */
#define GetProductOrderID @"http://tophot.host.smartgslb.com/?m=api&c=createOrder&a=createOrder"
/** 获取微信的预支付订单 */
#define GetWeChatPrepareID @"http://tophot.host.smartgslb.com/?m=api&c=weixin&a=callWeixin"




/**     发布的API      **/
/** 发布咨询 */
#define PublishConsult @"http://tophot.host.smartgslb.com/?m=api&c=question&a=createQuestion"
/** 发布日记 */
#define PublishDiary @"http://tophot.host.smartgslb.com/?m=api&c=diary&a=createArticle"
/** 获取日记本列表 */
#define GetNotebookList @"http://tophot.host.smartgslb.com/?m=api&c=diary&a=blogList"
/** 获取课程项目列表 + 用户的课程列表 */
#define GetProjectsAndUserCoursesList @"http://tophot.host.smartgslb.com/?m=api&c=diary&a=projectList"
/** 创建日记本 */
#define CreatNotebook @"http://tophot.host.smartgslb.com/?m=api&c=diary&a=createBlog"

'''



a = re.findall(r'"(.*)"', string);
# 抓出所有在双引号之间的内容

print('网址总数: ' , len(a))

# 遍历访问网址
for idx, val in enumerate(a):

  r = requests.get(val, timeout = 2)
  
  if r.status_code == 200:
    print('[',idx,']', 200,':', r.url)
  elif r.status_code == 404:
    print('失败: ', r.url)
    fp.write(r.url)
    fp.write('\n')

  
 
