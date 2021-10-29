import CSDataBase
import Derictory
from ExcelWork import ExcelWork
import os


def main():
    path = os.getcwd() + "/../Config"
    path = path.replace("\\", "/")
    list = Derictory.GetDirFileList(path)

    configPath = os.getcwd() + "/../ToolExcel/Assets/Configs"
    configPath = configPath.replace("\\", "/")

    BinPath = os.getcwd() + "/../ToolExcel/Assets/StreamingAssets/Bin"
    BinPath = BinPath.replace("\\", "/")

    Derictory.DeleteDirFile(BinPath)
    Derictory.DeleteDirFile(configPath)

    CSDataBase.WriteDataBase(configPath)
    for workpath in list:
        print("文件名:"+workpath)
        item = ExcelWork(workpath)
        item.ExportBin(BinPath)
        item.ExportCS(configPath)

    print("导出成功")

main()