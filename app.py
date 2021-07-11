# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from controllers.login_controller import LoginController

from PyQt5 import QtCore, QtGui, QtWidgets

from views.qt_login import Ui_qtlogin


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    qtlogin = QtWidgets.QMainWindow()
    ui = Ui_qtlogin()
    ui.setupUi(qtlogin)
    qtlogin.show()
    sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
