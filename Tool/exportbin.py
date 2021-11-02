import CSDataBase
import Derictory
from ConfigExcelWork import ConfigExcelWork
import os
import EnumUtils


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

    EnumPath = path + "/__CommonType.xlsx"
    EnumPath = EnumPath.replace("\\", "/")
    EnumUtils.Init(EnumPath)
    EnumUtils.ExportCS(configPath)
    CSDataBase.WriteDataBase(configPath)
    for workpath in list:
        print("文件名:"+workpath)
        enumFind = workpath.find("__")
        if enumFind > -1:
            continue
        item = ConfigExcelWork(workpath)
        item.ExportBin(BinPath)
        item.ExportCS(configPath)

    print("导出成功")

main()