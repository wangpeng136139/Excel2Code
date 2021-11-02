from typing import List, Tuple
import xlrd

from ConfigExcelData import ConfigExcelData


class ConfigExcelRowParent:
    datalist: List = []

    def GetValue(self, index):
        return self.datalist[index].GetValue()


class ConfigExcelRowTitle:
    def __init__(self, row, type) -> None:
        self.__datalist = []
        rowCount = len(row)
        for i in range(rowCount):
            cell = row[i]
            item = ConfigExcelData("", cell, type.GetValue(i), "")
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
            

    def GetMainKey(self) -> List:
        mainKeyList: List = []
        for item in self.__datalist:
            if item.IsMainKey() == True:
                mainKeyList.append(item)

        for item in self.__datalist:
            if item.IsSecondKey() == True:
                mainKeyList.append(item)

        if len(mainKeyList) < 1:
            mainKeyList.append(self.__datalist[0])
        
        return mainKeyList
        

        
class ConfigExcelRowType:
    def __init__(self, row) -> None:
        self.__datalist = []
        for cell in row:
           item = ConfigExcelData(cell, "", "", "")
           self.__datalist.append(item)

    def GetValue(self, index):
        return self.__datalist[index].GetValue()
        


class ConfigExcelRowMark:
    def __init__(self, row) -> None:
        self.__datalist: List = [] 
        for cell in row:
           item = ConfigExcelData(cell, "", "", "")
           self.__datalist.append(item)

    def GetValue(self, index):
        return self.__datalist[index].GetValue()
        

class ConfigExcelRow:
    def __init__(self, row, title, type, mark, colCount) -> None:
        self.__datalist = []
        rowCount = len(row)
        for i in range(0, colCount):
            if i < rowCount:
                cell = row[i]
            else:
                cell = ""
            
            titleValue = title.GetValueName(i)

            typeValue = type.GetValue(i).lower()
            markValue = mark.GetValue(i)
            item = ConfigExcelData(cell, titleValue, typeValue, markValue)
            self.__datalist.append(item)
        
    def GetCellBinList(self) -> list:
        cellList = []
        for cell in self.__datalist:
            cellList.append(cell.GetBytes())
        return cellList

    def GetCellBin(self, index) -> list:
        return self.__datalist[index].GetBytes()
