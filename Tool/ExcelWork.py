from typing import Dict
from typing import List
from ExcelSheel import ExcelSheel
from BinWrite import BinWrite
import xlrd
import ExcelUtils
import os


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

    def ExportBin(self, path: str):
        path = os.path.join(path, self.__workName + ".bin")
        rowCount = self.GetRowCount()   
        binWrite = BinWrite(path)
        binWrite.WriteInt(rowCount)
        for sheet in self.__sheetList:
            list = sheet.GetBinList()
            binWrite.WriteBin(list)

    def GetRowCount(self) -> int:
        count = 0
        for sheet in self.__sheetList:
            count = count + sheet.GetRowCountself()
        return count

    def ExportCS(self, path: str):
        path = os.path.commonpath(path, self.__workName + ".cs")
        return
        
        

    
