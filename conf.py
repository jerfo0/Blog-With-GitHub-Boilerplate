# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
enable_jsdelivr = {
    "enabled": True,
    "repo": "jerfo0/Blog-With-GitHub-Boilerplate@gh-pages"
}

# 站点设置
site_name = "生活碎片"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-18T16:51+08:00"
author = "杰夫"
email = "jerfo0@vip.qq.com"
author_homepage = "https://www.it520.org"
description = "记录零零碎碎..."
key_words = ['就爱吾妻', '9i57', '杰夫', 'blog']
language = 'zh-CN'
external_links = [
    {
        "name": "it520",
        "url": "https://www.it520.org/",
        "brief": "杰夫的个人博客"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "B站",
        "url": "https://space.bilibili.com/19128387",
        "icon": "gi gi-bilibili"
    },
  
    {
        "name": "Weibo",
        "url": "https://weibo.com/jerfo0",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
