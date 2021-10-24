from Derictory import GetDirFileList
from ExcelWork import ExcelWork
import os

def main():
    path = os.getcwd() + "/../Config"
    path = path.replace("\\", "/")
    list = GetDirFileList(path)
    for workpath  in list:
        item = ExcelWork(workpath)


main()