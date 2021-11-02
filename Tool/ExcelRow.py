from ExcelCell import ExcelCell


class ExcelRow:
    def __init__(self, row, colCount) -> None:
        self.__datalist = []
        rowCount = len(row)
        for i in range(0, colCount):
            if i < rowCount:
                cell = row[i]
            else:
                cell = ""
            item = ExcelCell(cell)
            self.__datalist.append(item)

    def GetValue(self, index: int) -> str:
        return self.__datalist[index].GetValue()

    def GetValueStr(self, index: int) -> str:
        return self.__datalist[index].GetValueStr()