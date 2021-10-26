from typing import List, Tuple
from ExcelData import ExcelData
import xlrd


class ExcelRowParent:
    datalist: List = []

    def GetValue(self, index):
        return self.datalist[index].GetValue()


class ExcelRowTitle:
    __datalist: List = []

    def GetValue(self, index):
        return self.__datalist[index].GetValue()

    def __init__(self, row) -> None:
        for cell in row:
           item = ExcelData(cell, "", "", "")
           self.__datalist.append(item)

    def GetMainKey(self) -> List:
        mainKeyList: List = []
        for item in self.__datalist:
            if item.IsMainKey() == True:
                mainKeyList.append(item)

        for item in self.__datalist:
            if item.IsSecondKey() == True:
                mainKeyList.append(item)

        if len(mainKeyList) < 1:
            mainKeyList.append(item)
        
        return mainKeyList
        

        
class ExcelRowType:
    __datalist: List = []

    def GetValue(self, index):
        return self.__datalist[index].GetValue()
        
    def __init__(self, row) -> None:
        for cell in row:
           item = ExcelData(cell, "", "", "")
           self.__datalist.append(item)


class ExcelRowMark:
    __datalist: List = []

    def GetValue(self, index):
        return self.__datalist[index].GetValue()
        
    def __init__(self, row) -> None:
        for cell in row:
           item = ExcelData(cell, "", "", "")
           self.__datalist.append(item)


class ExcelRow:
    __datalist: List = []

    def __init__(self, row, title, type, mark, colCount) -> None:
        rowCount = len(row)
        for i in range(0, colCount):
            if i < rowCount:
                cell = row[i]
            else:
                cell = ""
            
            titleValue = title.GetValue(i)
            findIndex = titleValue.find("#")
            if findIndex > -1:
                continue

            typeValue = type.GetValue(i).lower()
            markValue = mark.GetValue(i)
            item = ExcelData(cell, titleValue, typeValue, markValue)
            self.__datalist.append(item)
        
    def GetCellBinList(self) -> list:
        cellList = []
        for cell in self.__datalist:
            cellList.append(cell.GetBytes())
        return cellList
