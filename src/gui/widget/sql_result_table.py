from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class SqlResultTable(QTableWidget):
    def put_data(self, columns, values):
        self.setColumnCount(len(columns))
        self.setRowCount(len(values))

        self.setHorizontalHeaderLabels(columns)

        for row_num, row in enumerate(values):
            for col_num, val in enumerate(row):
                self.setItem(row_num, col_num, QTableWidgetItem(str(val)))

        self.resizeColumnsToContents()
