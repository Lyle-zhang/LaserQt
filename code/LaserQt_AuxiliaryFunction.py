# -*- coding: utf-8 -*-
import platform
import time

'''
@author  : Zhou Jian
@email   : zhoujian@hust.edu.cn
@version : V1.0
@date    : 2016.11.12
'''

# 检查当前操作系统版本信息并依此设置主路径
def check_os():
    if platform.system() == "Windows":
        return "C:/"
    elif platform.system() == "Linux":
        import getpass
        user = getpass.getuser()
        return "/home/" + user + "/"

# 获取当前屏幕尺寸
def get_current_screen_size():
    width = 1440
    height = 720
    return (width, height)

# 获取当前系统时间
def get_current_screen_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
