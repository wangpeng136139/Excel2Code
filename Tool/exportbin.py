import Derictory
from ConfigExcelWork import ConfigExcelWork
import os
import sys
import EnumUtils
import ColorHelper
import sys;
import yaml;

def main():
    os.chdir(os.sys.path[0]);
    try:
        yamlPath = os.path.join(os.getcwd(),"__Path.yaml");
        yamlPath = yamlPath.replace("\\","/");
        f = open(yamlPath,'r',encoding='utf-8')
        yamlContent = yaml.load(f,Loader=yaml.FullLoader)
        configPath =  yamlContent["Path"]["XlsxPath"];
        BinPath =  yamlContent["Path"]["BinPath"];
        CodePath =  yamlContent["Path"]["CodePath"];
        CodeType =  yamlContent["Path"]["CodeType"];
    except:
        ColorHelper.printRed(yamlPath + " is error");
        sys.exit();

    templatePath =os.path.join(os.getcwd(),"template","csharp"); 
    templatePath = templatePath.replace("\\","/");
    print("curl path: " +  os.getcwd())
    print("xlxs path: " + CodePath)
    print("code path: " + configPath)
    print("bin path: " + BinPath)
    print("template path" + templatePath)

    Derictory.CreateDir(BinPath)
    Derictory.CreateDir(CodePath)
    Derictory.DeleteDirFile(BinPath)
    Derictory.DeleteDirFile(CodePath)
    
     #拷贝公共代码到对应目录
    Derictory.CopyDirToDes(templatePath + "/common", CodePath);
    try:
        EnumPath = os.path.join(configPath, "__CommonEnum.xlsx");
        EnumPath = EnumPath.replace("\\", "/")
        EnumUtils.Init(EnumPath)
        EnumUtils.ExportCS(CodePath);
    except:
        ColorHelper.printRed("__CommonEnum.xlsx is error");
        sys.exit();

    filelist = Derictory.GetDirFileList(configPath)
    for i in range(0,len(filelist)):
        workpath = filelist[i]
        print("file path:"+workpath)
        enumFind = workpath.find("__CommonEnum");
        if enumFind > -1 or workpath.find(".xlsx") < 0:
            continue
        item = ConfigExcelWork(workpath)
        item.ExportBin(BinPath) 
        item.ExportCS(CodePath,templatePath)

    print("success");

main()