from typing import Dict
from typing import List
import xlrd
from ExcelSheel import ExcelSheel
import ExcelUtils
import os
import Derictory


class ExcelWork:
    __sheetList: List = []
    __sheetDic: Dict = {}
    __workName: str = ""

    def __init__(self, path: str) -> None:
        workBook = ExcelUtils.GetXLSX(path)
        if workBook is None:
            print("path is error:" + path)
            return
        self.__workName = os.path.basename(path).split('.')[0]
        workSheets = workBook.sheets()
        if workSheets is None:
            print("sheets is none:" + path)
        for sheet in workSheets:
            excelSheet = ExcelSheel(sheet)
            self.__sheetList.append(excelSheet)
            self.__sheetDic[excelSheet.GetName()] = excelSheet


    def GetAllSheetRowList(self) -> List:
        sheetRowList = []
        for sheet in self.__sheetList:
            sheetRowList.extend(sheet.GetRowListByStart(1))
        return sheetRowList

    
        
        

    
