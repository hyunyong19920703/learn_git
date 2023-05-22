import os, sys

sys.path.append("C:\\Users\\user\\Desktop\\python_project\\python\\pyside_prac")

from PySide2 import QtWidgets, QtCore, QtGui
from imp import reload
from first_delegator.ui import my_widget
from first_delegator.model import camera_model
from first_delegator.handler import maya_handler
from pprint import pprint

reload(camera_model)
reload(maya_handler)
reload(my_widget)


class My_Main(QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlag(QtCore.Qt.WindowType(True))
        self.ui = my_widget.Ui_Form()
        self.ui.setupUi(self)
        
        self.cam_model = None
        self.proxy_model = QtCore.QSortFilterProxyModel()
        self.delegator = None
        
        self.connected()
        
    def connected(self):
        self.set_model()
    
    def set_model(self):
        row_datas = maya_handler.get_cam_items()
        self.cam_model = camera_model.Camera_Model(row_datas=row_datas)
        self.proxy_model.setSourceModel(self.cam_model)
        self.ui.tableView.setModel(self.proxy_model)
        
def run_main_maya():
    from maya import OpenMayaUI as mui
    from shiboken2 import wrapInstance
    mayaMainWindowPtr = mui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QtWidgets.QMainWindow)
    
    app = QtWidgets.QApplication.instance()
    excute_main = My_Main(mayaMainWindow) 
    excute_main.show()
    app.exec_()
        
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    
    main = My_Main()
    main.show()
    app.exec_()