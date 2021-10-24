import xlrd
import os.path


def GetXLSX(path: str):
    if os.path.exists(path) == False:
        return None
    workBook = xlrd.open_workbook(path)
    return workBook