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
        AddEnum(row.GetValue(1), row.GetValue(0), row.GetValue(2), row.GetValue(3))


def ExportCS(path):
    for k, v in __enumDic.items():
        cspath = path + "/" + k + ".cs"
        content = Content()
        content.WriteLine("namespace Config")
        content.StartBlock()
        content.WriteLine("public enum "+k)
        content.StartBlock()
        for item in v:
            content.WriteLine("//" + item.GetDes())
            content.WriteLine(item.GetValueStr() + " = " + item.GetIntStr() + " ,")

        content.EndBlock()
        content.EndBlock()
        content.WriteFile(cspath)


    

