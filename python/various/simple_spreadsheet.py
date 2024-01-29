from typing import Tuple
from typing import Union


class Spreadsheet(object):
    def __init__(self):
        self.spreadsheet = {}

    def set_cell(self, loc: str, value: Union[int, Tuple[str, str]]):
        if isinstance(value, int):
            self.spreadsheet[loc] = [value, ()]
        else:
            value1, value2 = value[0], value[1]
            sum = self.get_cell_value(value1) + self.get_cell_value(value2)
            self.spreadsheet[loc] = [sum, value]

    def get_cell_value(self, loc: str):
        cell = self.spreadsheet.get(loc, None)
        if cell:
            if len(cell[1]) == 2:
                cell1 = self.spreadsheet[loc][1][0]
                cell2 = self.spreadsheet[loc][1][1]
                real_value = self.get_cell_value(cell1) + self.get_cell_value(cell2)
                self.spreadsheet[loc][0] = real_value
            return self.spreadsheet[loc][0]
        return -1


def test_spreadsheet(s_class):
    sheet = s_class()

    # ints
    sheet.set_cell("A", 3)
    sheet.set_cell("B", 5)
    sheet.set_cell("C", 1)
    assert sheet.get_cell_value("B") == 5

    # formulas
    sheet.set_cell("D", ("B", "C"))
    assert sheet.get_cell_value("D") == 6

    sheet.set_cell("E", ("B", "D"))

    assert sheet.get_cell_value("E") == 11
    sheet.set_cell("F", ("E", "D"))

    assert sheet.get_cell_value("F") == 17

    # edits
    sheet.set_cell("C", ("B", "A"))
    # C = 1 -- OLD
    # C = B + A
    # D = 6 -- OLD
    # D = 13 -- NEW
    assert sheet.get_cell_value("C") == 8
    assert sheet.get_cell_value("D") == 13
    assert sheet.get_cell_value("E") == 18
    assert sheet.get_cell_value("F") == 31

    sheet.set_cell("A", 1)
    assert sheet.get_cell_value("F") == 27
    assert sheet.get_cell_value("C") == 6

    sheet.set_cell("D", ("A", "C"))
    assert sheet.get_cell_value("D") == 7
    assert sheet.get_cell_value("F") == 19

    print("Tests passed!!!!")


test_spreadsheet(Spreadsheet)
