from typing import List
from ExcelRow import ExcelRow, ExcelRowTitle, ExcelRowType, ExcelRowMark
import xlrd
import xlwt


# 第一行变量名 加#代表不写入，第一列一定是ID
#（Main）代表为主键，（Second）代表为第二主键，如果没有标注，以第一列ID为主键，暂时只支持主键
# 第二行是注释，或者备注，不写入
# 第三行是类型，int string bool enum等，大小写无所谓
# 第四行是具体数据的开始
class ExcelSheel:
    m_listrow: List = []
    m_name: str = ""
    m_rowTitle: ExcelRowTitle = ""
    m_rowMark: ExcelRowMark = ""
    m_rowType: ExcelRowType = ""

    def __init__(self, sheet) -> None:
        self.m_name = sheet.name
        self.m_rowTitle = ExcelRowTitle(sheet.row_values(0))
        self.m_rowMark = ExcelRowMark(sheet.row_values(1))
        self.m_rowType = ExcelRowType(sheet.row_values(2))
        
        rowcount = sheet.nrows
        colcount = sheet.ncols
        for i in range(3, rowcount):
            row = sheet.row_values(i)
            item = ExcelRow(row, self.m_rowTitle, self.m_rowType, self.m_rowMark, colcount)
            self.m_listrow.append(item)

