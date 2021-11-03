def Openfile(self):
        try:
            self.all_data = pd.read_csv("laptops.csv")

        except:
            print("Error Occurs")

        numrows = len(self.all_data.index)
        self.tableWidget.setColumnCount(len(self.all_data.columns))
        self.tableWidget.setRowCount(len(numRows))
        for i in range(numrows):
            for j in range(len(self.all_data.columns)):
                self.tableWidget.setItem(len(i, j, QTableWidget(str(self.all_data.iat[i, j]))))

        self.tableWidget.resizeColumnToContents()
        self.tableWidget.resizeRowsToContents()