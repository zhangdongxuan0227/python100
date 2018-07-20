#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/18 16:22
# @Author  : zhangxingchen
# @Site    : 
# @File    : 二维码.py
# @Software: PyCharm

import qrcode

img = qrcode.make("hello,qrcode")
img.save('test.png')


# 根据url生成二维码
def qrcodeWithUrl(url):
    img = qrcode.make(url)
    # 保存图片
    savePath = '1.png'
    img.save(savePath)
    print(img)


# 根据输入内容生成二维码
#
# def qrcodeWithText(text):
#     img = qrcode.make(text)
#     # 保存图片
#     savePath = '2.png'
#     img.save(savePath)
#     print(img)
#
#
# content = input('请输入内容：')
# if 'http' in content:
#     qrcodeWithUrl(content)
# else:
#     qrcodeWithText(content)
# print('二维码已生成！')
#



qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('qrcode.png')