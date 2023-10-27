import os
from typing import List
import shutil;
def DeleteDirFile(path):
    folder = ExistsDir(path)
    if not folder:
        return
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            DeleteDirFile(c_path)
        else:
            os.remove(c_path)


def CreateDir(path: str) -> None:
    folder = ExistsDir(path)
    if not folder:
        os.makedirs(path)


def DeleteDir(path: str) -> None:
    os.path.defpath(path)


def ExistsDir(path: str) -> bool:
    exists = os.path.exists(path)
    return exists


def ExistsFile(path: str) -> bool:
    exists = os.path.exists(path)
    return exists

def CopyDirToDes(from_file,to_file):
    if not os.path.exists(to_file):  # 如不存在目标目录则创建
        os.makedirs(to_file)
    files = os.listdir(from_file)  # 获取文件夹中文件和目录列表
    for f in files:
        if os.path.isdir(from_file + '/' + f):  # 判断是否是文件夹
            CopyDirToDes(from_file + '/' + f, to_file + '/' + f)  # 递归调用本函数
        else:
            shutil.copy(from_file + '/' + f, to_file + '/' + f)  # 拷贝文件


def GetDirFileList(path) -> List:
    list_name = []
    GetDirFile(path, list_name)
    return list_name


def GetDirFile(path, list_name: List) -> None:  #传入存储的list
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            GetDirFile(file_path, list_name)
        else:
            file_path = file_path.replace("\\","/")
            list_name.append(file_path)