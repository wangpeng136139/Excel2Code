from typing import Dict
from typing import List
from ExcelSheel import ExcelSheel
import xlrd
import xlwt
import ExcelUtils


class ExcelWork:
    sheetList: List = []
    sheetDic: Dict = {}

    def __init__(self, path: str) -> None:
        workBook = ExcelUtils.GetXLSX(path)
        if workBook is None:
            print("path is error:" + path)
            return
        workSheets = workBook.sheets()
        if workSheets is None:
            print("sheets is none:" + path)
        for sheet in workSheets:
            excelSheet = ExcelSheel(sheet)
            self.sheetList.append(excelSheet)
            self.sheetDic[excelSheet.m_name] = excelSheet

    def ExportBin(path: str):
        
        return


    def ExportCS(path: str):
        return
        
        

    
