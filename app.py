

from PyQt5 import QtCore, QtGui, QtWidgets

from views.main_screen import Ui_MainLounge

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainLounge = QtWidgets.QWidget()
    ui = Ui_MainLounge()
    ui.setupUi(MainLounge)
    MainLounge.showFullScreen()
    sys.exit(app.exec_())


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
