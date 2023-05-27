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
        
        # config table view
        self.ui.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.ui.tableView.customContextMenuRequested.connect(self.context_menu)
        
        # config item model
        self.cam_model = None
        self.proxy_model = QtCore.QSortFilterProxyModel()
        self.delegator = camera_model.Prac_Delegator()
        self.ui.tableView.setItemDelegate(self.delegator)
        
        # connect functions
        self.connected()
        
    def connected(self):
        self.set_model()
        self.delegator.box_clicked.connect(self.boxes_state_changed)
    
    @QtCore.Slot(QtCore.QPoint)
    def context_menu(self, pos):
        viewport = self.ui.tableView.viewport()
        menu = QtWidgets.QMenu(viewport)
        
        menuItem_01 = menu.addAction('dev - print')
        menuItem_01.triggered[()].connect(self.dev_print)
        
        menu.exec_(viewport.mapToGlobal(pos))
        
    def get_selected_indexes(self):
        
        indexes = self.ui.tableView.selectedIndexes()
        row_datas = list()
        
        for index in indexes:
            column = index.column()
            if column == 0:
                row_data = self.proxy_model.data(index, role=QtCore.Qt.UserRole)
                row_datas.append(row_data)
            
        return row_datas
        
    def dev_print(self):
        
        row_datas = self.get_selected_indexes()
        
        for row in row_datas:
            
            print(row.name)
            print(row.type)
            print(row.checked)
            pprint(row.boxes_value)
    
    def set_model(self):
        row_datas = maya_handler.get_cam_items()
        self.cam_model = camera_model.Camera_Model(row_datas=row_datas)
        self.proxy_model.setSourceModel(self.cam_model)
        self.ui.tableView.setModel(self.proxy_model)
        self.set_delegate()
        self.ui.tableView.resizeColumnsToContents()
        self.ui.tableView.resizeRowsToContents()
        
    def set_delegate(self):
        for row in range(self.proxy_model.rowCount()):
            for column in range(self.proxy_model.columnCount()):
                index = self.proxy_model.index(row, column)
                self.ui.tableView.openPersistentEditor(index)
    
    def boxes_state_changed(self, index, check_box, state):
        # print(index)
        # print(check_box)
        # print(state)
        
        self.proxy_model.setData(index, check_box, QtCore.Qt.UserRole)
        
        
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