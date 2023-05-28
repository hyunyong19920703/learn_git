import os, sys
import typing

from PySide2 import QtWidgets, QtGui, QtCore
from pprint import pprint
from glob import glob
from imp import reload

from Alembic_Exporter.ui import Abc_Expoter_UI
from Alembic_Exporter.handler import maya_handler
from Alembic_Exporter.model import selected_obj_model

reload(Abc_Expoter_UI)
reload(maya_handler)
reload(selected_obj_model)

class AE_Main(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowFlag(QtCore.Qt.WindowType(True))
        self.ui = Abc_Expoter_UI.Ui_Alembic_Expoter_Widget()
        self.ui.setupUi(self)
        
        self.asset_tree_model = None
        
        
        self.connected()
        
    def connected(self):
        self.set_model()
        
    def set_model(self):
        get_assets = maya_handler.get_asset_model_from_current_scene()
        self.asset_tree_model = selected_obj_model.Selected_Asset_Model(row_datas=get_assets)
        self.ui.Model_Tv.setModel(self.asset_tree_model)
        self.ui.Model_Tv.expandAll()
        


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
    


