from typing import List, Tuple
import xlrd

from ConfigExcelData import ConfigExcelData


class ConfigExcelRowTitle:
    def __init__(self, row, type,mark) -> None:
        self.__datalist = []
        colCount = len(row)
        for i in range(colCount):
            cell = row[i]
            item = ConfigExcelData("", cell, type.GetValue(i), mark.GetValue(i), True)
            self.__datalist.append(item)

    def GetValue(self, index):
        return self.__datalist[index].GetValue()
    
    def GetValueName(self, index):
        return self.__datalist[index].GetValueName()

    def GetCSReadValueList(self) -> List:
        csList = []
        for item in self.__datalist:
            csList.append(item.GetCSReadValue())
        return csList

    def GetCSMarkList(self) -> List:
        csList = []
        for item in self.__datalist:
            csList.append(item.GetCSMarkValue())
        return csList

    def GetCSGetValueList(self) -> List:
        csList = []
        for item in self.__datalist:
            csList.append(item.GetCSGetValue())
        return csList

    def GetCSClassValue(self) -> List:
        csList = []
        for item in self.__datalist:
            csList.append(item.GetCSClassValue())
        return csList

    def GetCount(self) -> int:
        return len(self.__datalist)
            
    def GetMainKey(self) -> List:
        mainKeyList: List = []
        for item in self.__datalist:
            if item.IsMainKey() == True:
                mainKeyList.append(item)

        for item in self.__datalist:
            if item.IsSecondKey() == True:
                mainKeyList.append(item)
        
        return mainKeyList


class ConfigExcelRowType:
    def __init__(self, row) -> None:
        self.__datalist = []
        for cell in row:
           item = ConfigExcelData(cell, "", "", "", False)
           self.__datalist.append(item)

    def GetValue(self, index):
        return self.__datalist[index].GetValue()
        

class ConfigExcelRowMark:
    def __init__(self, row) -> None:
        self.__datalist: List = [] 
        for cell in row:
           item = ConfigExcelData(cell, "", "", "", False)
           self.__datalist.append(item)

    def GetValue(self, index):
        return self.__datalist[index].GetValue()

    def GetCount(self) -> int:
        return len(self.__datalist)


class ConfigExcelRow:
    def __init__(self, row, title, type, mark) -> None:
        self.__datalist = []
        colCount = len(row)
        for i in range(0, colCount):
            if i < colCount:
                cell = row[i]
            else:
                cell = ""
            
            titleValue = title.GetValueName(i)

            typeValue = type.GetValue(i).lower()
            markValue = mark.GetValue(i)
            item = ConfigExcelData(cell, titleValue, typeValue, markValue, False)
            self.__datalist.append(item)
        
    def GetCellBinList(self) -> list:
        cellList = []
        for cell in self.__datalist:
            cellList.append(cell.GetBytes())
        return cellList

    def GetCellBin(self, index) -> list:
        return self.__datalist[index].GetBytes()


class DataExcelRow:
    def __init__(self, firstRow, curRow) -> None:
        self.__datalist = []
        for i in range(0, len(firstRow)):
            value = firstRow[i]
            if value.find("#") > -1:
                continue
            self.__datalist.append(curRow[i])

    def __len__(self):
        return len(self.__datalist)
    
    def __getitem__(self, key):
        return self.__datalist[key]
