from CSDataBase import WriteDataBase
from Derictory import GetDirFileList
from ExcelWork import ExcelWork
import os

def main():
    path = os.getcwd() + "/../Config"
    path = path.replace("\\", "/")
    list = GetDirFileList(path)
    WriteDataBase("D:/MyProject/ExportExcel/ToolExcel/Assets/Configs")
    for workpath  in list:
        item = ExcelWork(workpath)
        item.ExportBin("D:/MyProject/ExportExcel/ToolExcel/Assets/StreamingAssets/Bin")


main()