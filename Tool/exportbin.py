import CSDataBase
import Derictory
from ConfigExcelWork import ConfigExcelWork
import os
import sys
import EnumUtils


def main():
    
    # 配置路径
    path = sys.argv[1] 
    path = path.replace("\\", "/")
    # 导出代码路径
    configPath = sys.argv[2] 
    configPath = configPath.replace("\\", "/")
    # 导出bin文件路径
    BinPath = sys.argv[3] 
    BinPath = BinPath.replace("\\", "/")

    print("配置路径: " + path)
    print("导出代码路径: " + configPath)
    print("导出bin文件路径: " + BinPath)

    list = Derictory.GetDirFileList(path)

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