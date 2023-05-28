import os, sys
import typing

from PySide2 import QtWidgets, QtGui, QtCore
from pprint import pprint
from glob import glob
from imp import reload

from Alembic_Exporter.ui import Abc_Expoter_UI

reload(Abc_Expoter_UI)


class AE_Main(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowFlag(QtCore.Qt.WindowType(True))
        self.ui = Abc_Expoter_UI.Ui_Alembic_Expoter_Widget()
        self.ui.setupUi(self)
        


def main():
    app = QtWidgets.QApplication()
    excute_main = AE_Main()
    excute_main.show()
    
    app.exec_()
    
def maya_main_run():
    from maya import OpenMayaUI as mui
    from shiboken2 import wrapInstance
    mayaMainWindowPtr = mui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QtWidgets.QMainWindow)

    global app
    app = QtWidgets.QApplication.instance()
    excute_main = AE_Main(mayaMainWindow) 
    excute_main.show()
    app.exec_()
    
if __name__ == '__main__':
    main()
    


