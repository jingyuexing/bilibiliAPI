# -*- coding: utf-8 -*-
# @Author: Admin
# @Date:   2021-05-27 07:45:23
# @Last Modified by:   Admin
# @Last Modified time: 2021-05-27 08:51:42

import sys,os
sys.path.append(os.path.dirname(__file__)+ os.sep + '../')
from Bilibili import User,Video,Article


def test_User():
    user = User(546195)
    print(user.birthday)
    print(user.mid)
    print(user.level)


def test_Article():
    # like https://www.bilibili.com/read/cv11442795
    # this digits is article number
    article = Article(11442795)
    print(f"文章{article.title}")
    print(f"此文章投币数是:{article.coin}")
    print(f"此文章点赞数为:{article.like}")
    print(f"此文章阅读数为:{article.read}")


def test_Video():
    video = Video("BV1BS4y1Y73G")
    print(f'视频封面:{video.cover}')
    print(f'视频点赞数:{video.like}')
    print(f'视频投币数:{video.coin}')
    print(f'视频上传时间:{video.createTime}')
    print(f'视频收藏数:{video.favorite}')
    print(video.getReply(1))


def main():
    # test_User()
    # test_Article()
    test_Video()


if __name__ == '__main__':
    main()
