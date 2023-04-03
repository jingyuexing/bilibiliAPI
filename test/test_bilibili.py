# -*- coding: utf-8 -*-
# @Author: Admin
# @Date:   2021-05-27 07:45:23
# @Last Modified by:   Admin
# @Last Modified time: 2021-05-27 08:51:42

import sys,os
import unittest
sys.path.append(os.path.dirname(__file__)+ os.sep + '../')
from Bilibili import User,Video,Article,getOnlineNumber
from unittest import TestCase

class TestApi(TestCase):
    def testVideoApi(self):
        video = Video("BV1BS4y1Y73G")
        self.assertTrue(expr=video.cover != "", msg="the video loading failed")

    def testArticleApi(self):
        article = Article(11442795)
        self.assertTrue(expr=article.title != "",msg="the loading article title failed")

    def testUserApi(self):
        user = User(546195)
        self.assertTrue(expr=user.face != "",msg="the user infor API testing failed")

    def testUserCard(self):
        online = getOnlineNumber()
        self.assertTrue(expr=online != None,msg="online number API testing failed")

if __name__ == '__main__':
    unittest.main()
