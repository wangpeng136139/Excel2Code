from typing import List
from ConfigExcelRow import ConfigExcelRow, ConfigExcelRowTitle, ConfigExcelRowType, ConfigExcelRowMark, DataExcelRow
import xlrd
from CommonType import VariableType;
from CommonType import CodeType;


# 第一行变量名 加#代表不写入，第一列一定是ID
#（Main）代表为主键，（Second）代表为第二主键，如果没有标注，以第一列ID为主键，暂时只支持主键
# 第二行是注释，或者备注，不写入
# 第三行是类型，int string bool enum等，大小写无所谓
# 第四行是具体数据的开始
class ConfigExcelSheel:
    def __init__(self, sheet) -> None:
        self.__name = sheet.name
     
        firstRow = sheet.row_values(0)
        cullRow = DataExcelRow(firstRow, firstRow)
        self.__listrow = [];
        self.__rowMark = ConfigExcelRowMark(DataExcelRow(firstRow, sheet.row_values(1)))
        self.__rowType = ConfigExcelRowType(DataExcelRow(firstRow, sheet.row_values(2)))
        self.__rowTitle = ConfigExcelRowTitle(DataExcelRow(firstRow, sheet.row_values(0)), self.__rowType,self.__rowMark);

        self.__rowcount = sheet.nrows
        self.__colcount = len(cullRow)
        for i in range(3, self.__rowcount):
            row = sheet.row_values(i)       
            item = ConfigExcelRow(DataExcelRow(firstRow, row), self.__rowTitle, self.__rowType, self.__rowMark)
            self.__listrow.append(item)


    def GetName(self) -> str:
        return self.__name

    def GetRowCount(self) -> int:
        return self.__rowcount

    def GetVariableType(self,codeType:CodeType):
        return self.__rowTitle.GetVariableType(codeType);

    def GetGetVariableRead(self,codeType:CodeType) -> List:
        return self.__rowTitle.GetGetVariableRead(codeType);

    def GetMarkList(self) -> List:
        return self.__rowTitle.GetMarkList()


    def GetVariable(self,codeType:CodeType) -> List:
        return self.__rowTitle.GetVariable(codeType)

    def GetTypeToRead(self,codeType:CodeType) -> List:
        return self.__rowTitle.GetTypeToRead(codeType)



    def GetMainKey(self) -> List:
        return self.__rowTitle.GetMainKey()

    def GetBinList(self) -> List:
        binList: List = []
        list = self.__listrow
        for index in range(len(list)):
            row = list[index]
            for colIndex in range(self.__colcount):
                binList.append(row.GetCellBin(colIndex))
        return binList
            
