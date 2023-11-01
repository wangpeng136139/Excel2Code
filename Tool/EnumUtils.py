from Content import Content
from Derictory import ExistsFile
from EnumData import EnumData
from ExcelWork import ExcelWork


__enumDic = {}


def AddEnum(enum: str, value: str, index: int, des: str) -> bool:
    if len(enum) < 1 or len(value) < 1:
        return False
    item = EnumData(value, enum, index, des)
    dicList = []
    if enum in __enumDic:
        dicList = __enumDic[enum]
    dicList.append(item)
    __enumDic[enum] = dicList
    return True


def GetIndex(enum: str, value: str) -> int:
    dicList = []
    if enum in __enumDic:
        dicList = __enumDic[enum]
    for item in dicList:
        if item.GetValue() == value:
            return item.GetInt()  
    return -1


def ClearEnum() -> None:
    enumDic = {}

def Init(path: str):
    if ExistsFile(path):
        InitByWork(ExcelWork(path))

def InitByWork(work: ExcelWork) -> None:
    ClearEnum()
    listRow = work.GetAllSheetRowList()
    if listRow == None or len(listRow) < 1:
        return
    
    for row in listRow:
        try:
            AddEnum(row.GetValue(1), row.GetValue(0), row.GetValue(2), row.GetValue(3))
        except:
            ColorHelper.printRed("__CommonEnum.xlsx "+ row.GetValue(1) +" is error");
            sys.exit();


def ExportCpp(path):
    cspath = path + "/CommonEnum.h"
    content = Content()
    for k, v in __enumDic.items():
        content.WriteLine("enum "+k)
        content.StartBlock()
        for item in v:
            content.WriteLine("//" + item.GetDes())
            content.WriteLine(item.GetValueStr() + " = " + item.GetIntStr() + " ,")
        content.EndBlock()
        content.WriteLine("\n");
    content.WriteLine(";");    
    content.WriteFile(cspath)

def ExportCS(path):
    for k, v in __enumDic.items():
        cspath = path + "/" + k + ".cs"
        content = Content()
        content.WriteLine("namespace TableConfig")
        content.StartBlock()
        content.WriteLine("public enum "+k)
        content.StartBlock()
        for item in v:
            content.WriteLine("//" + item.GetDes())
            content.WriteLine(item.GetValueStr() + " = " + item.GetIntStr() + " ,")

        content.EndBlock()
        content.EndBlock()
        content.WriteFile(cspath)


def ExportJava(path,javaPackage):
    for k, v in __enumDic.items():
        cspath = path + "/" + k + ".java"
        content = Content()
        content.WriteLine("package "+javaPackage+";");
        content.WriteLine("public enum "+k)
        content.StartBlock()
        for item in v:
            content.WriteLine("//" + item.GetDes())
            content.WriteLine(item.GetValueStr() + "(" + item.GetIntStr() + "),")
        content.WriteLine(";");

        content.WriteLine(k + "(int v)");
        content.StartBlock();
        content.WriteLine("this."+k+"=v;");
        content.EndBlock();

        content.WriteLine("public int Get"+k+"()");
        content.StartBlock();
        content.WriteLine("return "+k+";");
        content.EndBlock();

        content.WriteLine("private final int "+k+";");

        
        content.WriteLine("public static "+k+" fromInt(int v)");
        content.StartBlock();
        content.WriteLine("switch (v)");
        content.StartBlock();
        for item in v:
            content.WriteLine("case "+ item.GetIntStr() + ":");
            content.WriteLine("return " +  item.GetValueStr() + ";");
        content.EndBlock();
        content.WriteLine("return null; ");
        content.EndBlock();


        content.EndBlock()
        content.WriteFile(cspath)

