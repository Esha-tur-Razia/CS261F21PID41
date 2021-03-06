# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'laptopster.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(839, 614)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255, 85, 0)")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 110, 151, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 180, 151, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(620, 10, 141, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 230, 721, 351))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(9)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(590, 120, 171, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(590, 90, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(170, 0, 201, 20))
        self.label_5.setStyleSheet("font: 11pt \"Papyrus\";\n"
"color: rgb(255, 85, 0);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(340, 40, 231, 181))
        self.label_6.setStyleSheet("background-image: url(:/laptopster/laptop-circle-swoosh-icon-logo-260nw-336320570 (1).jpg);")
        self.label_6.setText("")
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 839, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(100, 100, 600, 400)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

        # method for widgets

    def UiComponents(self):

        # creating a push button
        button = QPushButton("CLICK", self)

        # setting geometry of button
        button.setGeometry(200, 150, 100, 30)

        # adding action to a button
        button.clicked.connect(self.Load data)

        # action method

    def clickme(self):

        # printing pressed
        print("pressed")

    # create pyqt5 app
    App = QApplication(sys.argv)
    window = Window()

    # start the app
    sys.exit(App.exec())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Laptopster"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Insertion-sort"))
        self.combo_box.activated.connect(insertionsort)
        # method called by combo box

            def insertionsort(arr,self):
                # for loop iteration in python from j to the length of array
                j = 1
                for j in range(len(arr)):
                    key = arr[j]
                    i = j - 1
                while i > 0 and arr[i] < key:
                    arr[i + 1] = arr[i]
                    i = i - 1
                arr[i + 1] = key

            def print_List(arr):
                for i in range(len(arr)):
                    print(arr[i], end=" ")

            print(insertionsort)
        self.comboBox.setItemText(1, _translate("MainWindow", "Merge-sort"))
        self.combo_box.activated.connect(mergesort)

        # method called by combo box


        def Merge_Sort(arr,self):
             first = []
             second = []
            if len(arr) > 1:
               mid = len(arr) // 2
               first = arr[:mid]
               second = arr[mid:]
               Merge_Sort(first)
               Merge_Sort(second)
               i = 0
               j = 0
               k = 0
        while i < len(first) and j < len(second):
            if first[i] < second[j]:
                arr[k] = first[i]
                i = i + 1
            else:
                 arr[k] = second[j]
                 j = j + 1
                 k = k + 1

        while i < len(first):
              arr[k] = first[i]
              i = i + 1
              k = k + 1

        while j < len(second):
              arr[k] = second[j]
              j = j + 1
              k = k + 1


        def print_List(arr):
            for i in range(len(arr)):
                print(arr[i], end=" ")

        print(mergesort)

        self.comboBox.setItemText(2, _translate("MainWindow", "bubble-sort"))
        self.combo_box.activated.connect(bubblesort)

        # method called by combo box
        def bubblesort(self,arr):

            for i in range(len(arr) - 1):
                 min = i
                for j in range(i + 1, len(arr)):
                    if (arr[j] < arr[min]):
                         min = j
                    if (min != i):
                        arr[i], arr[min] = arr[min], arr[i]
                return arr

            print(bubblesort)
        self.comboBox.setItemText(3, _translate("MainWindow", "Counting-sort"))
        self.combo_box.activated.connect(countingsort)

        # method called by combo box


         import random, math
         def getKey(n):
         return n


        def countingSort(list, k, getKey,self):
            count = [0] * k


            for n in list
                count[getKey(n)] = count[getKey(n)] + 1
                for i in range(k)
                   if i == 0:
                      count[i] = count[i]
                   else:
                      count[i] += count[i - 1]
                      output = [None] * len(list)
                for i in range(len(list) - 1, -1, -1)
                    sortkey = getKey(list[i])
                    output[count[sortkey] - 1] = list[i]
                    count[sortkey] -= 1
                    return output
                    random.seed(0)
                    arr = [random.randint(0, 20) for n in range(10)]
                    print("Unsorted array")
                    print(arr)

          print(countingsort)
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Ascending"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Decending"))
        self.label_2.setText(_translate("MainWindow", "Select algorithm"))
        self.label_3.setText(_translate("MainWindow", "order of sorting"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Rating"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Memory"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Core"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Display"))
        self.label_4.setText(_translate("MainWindow", "Search by"))s
        self.label_5.setText(_translate("MainWindow", "A simple sorting application"))

        def Openfile(self):
            try:
                self.all_data = pd.read_csv(laptops.csv)

            except:
                print("Error Occurs")

        def dataHead(self):
            numrows = len(self.all_data.index)
            self.tableWidget.setColumnCount(len(self.all_data.columns))
            self.tableWidget.setRowCount(len(numRows))
            self.tableWidget.setHorizontalHeaderItem(len(self.all_data.columns))
            for i in range(numrows):
                     for j in range(len(self.all_data.columns)):
                         self.tableWidget.setItem(len(i,j,QTableWidget(str(self.all_data.iat[i,j])))

            self.tableWidget.resizeColumnToContents()
            self.tableWidget.resizeRowsToContents()

import test_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
