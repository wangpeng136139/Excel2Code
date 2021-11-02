from typing import List
import xlrd

from ExcelRow import ExcelRow


class ExcelSheel:
    __listrow: List = []
    __name: str = ""
    __rowCount: int = 0
    __colcount: int = 0

    def __init__(self, sheet) -> None:
        self.__name = sheet.name
        self.__rowcount = sheet.nrows
        self.__colcount = sheet.ncols       
        for i in range(0, self.__rowcount):
            row = sheet.row_values(i)
            item = ExcelRow(row, self.__colcount)
            self.__listrow.append(item)

    def GetName(self) -> str:
        return self.__name

    def GetColCount(self) -> int:
        return self.__colcount

    def GetRowCount(self) -> int:
        return self.__rowcount

    def GetRowList(self) -> List:
        return self.__listrow
    
    def GetRowListByStart(self, start) -> List:
        return self.__listrow[start:]

                


