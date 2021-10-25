from CSDataBase import WriteDataBase
from Derictory import GetDirFileList
from ExcelWork import ExcelWork
import os


def main():
    path = os.getcwd() + "/../Config"
    path = path.replace("\\", "/")
    list = GetDirFileList(path)

    configPath = os.getcwd() + "/../ToolExcel/Assets/Configs"
    configPath = configPath.replace("\\", "/")
    WriteDataBase(configPath)

    BinPath = os.getcwd() + "/../ToolExcel/Assets/StreamingAssets/Bin"
    BinPath = BinPath.replace("\\", "/")
    for workpath in list:
        print("文件名:"+workpath)
        item = ExcelWork(workpath)
        item.ExportBin(BinPath)
        item.ExportCS(configPath)


main()