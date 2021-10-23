from typing import List
from ExcelData import ExcelData
import xlrd
import xlwt

class ExcelRowParent:
    datalist: List = []

    def GetValue(self, index):
        return self.datalist[index].GetValue()


class ExcelRowTitle(ExcelRowParent):
    def __init__(self, row) -> None:
        for cell in row:
           item = ExcelData(cell, "", "", "")
           self.datalist.append(item)

        
class ExcelRowType(ExcelRowParent):
    def __init__(self, row) -> None:
        for cell in row:
           item = ExcelData(cell, "", "", "")
           self.datalist.append(item)


class ExcelRowMark(ExcelRowParent):
    def __init__(self, row) -> None:
        for cell in row:
           item = ExcelData(cell, "", "", "")
           self.datalist.append(item)


class ExcelRow:
    datalist: List = []

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
            self.datalist.append(item)