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
        
        self.scene_info = maya_handler.config_maya_setting()
        self.asset_tree_model = None   
        
        self.connected()        
        
    def connected(self):
        self.init_UI_info()
        self.set_model()
        self.ui.abc_export_pushButton.clicked.connect(lambda: self.export_alembic())
        
        
    def export_alembic(self):
        QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))        
        maya_handler.shape_deform()
        
        self.get_info_from_ui()
        
        selected_item_list = self.get_checked_item_list()
        
        ''' alembic export '''
        for sel in selected_item_list:
            item_dict = maya_handler.make_item_dict(sel, self.scene_info)
            pprint(item_dict)
    
        
        QtWidgets.QApplication.restoreOverrideCursor()
        
    
    
    def get_checked_item_list(self):
        
        checked_item_list = list()
        
        parent_index = QtCore.QModelIndex()
        for row in range(self.asset_tree_model.rowCount()):
            index = self.asset_tree_model.index(row, 0, parent_index)
            data = self.asset_tree_model.data(index, role=QtCore.Qt.UserRole)
            
            for child_row in range(self.asset_tree_model.rowCount(index)):
                child_index = self.asset_tree_model.index(child_row, 0, index)
                data = self.asset_tree_model.data(child_index, role=QtCore.Qt.UserRole)
                
                if data.checked is True:
                    checked_item_list.append(data.item)
                    
        return checked_item_list
            
    
        
        
    def get_info_from_ui(self):
        
        data_dict = self.scene_info
        
        selected_step = self.ui.step_comboBox.currentIndex()
        selected_blurstep = self.ui.blurstep_comboBox.currentIndex()
        data_dict['step'] = float(self.ui.step_comboBox.itemText(selected_step))
        data_dict['blur_step'] = float(self.ui.blurstep_comboBox.itemText(selected_blurstep))
        data_dict['pre_roll'] = int(self.ui.pre_roll_spinBox.value())
        data_dict['post_roll'] = int(self.ui.post_roll_spinBox.value())
        data_dict['start_frame'] = int(self.ui.startf_lineEdit.text()) - data_dict['pre_roll']
        data_dict['end_frame'] = int(self.ui.endf_lineEdit.text()) + data_dict['post_roll']
        data_dict['frame_range'] = [data_dict['start_frame'], data_dict['end_frame']]
        
        self.scene_info = data_dict
        
    
        
    def init_UI_info(self):        
        self.ui.startf_lineEdit.setText(str(self.scene_info['start_frame']))
        self.ui.endf_lineEdit.setText(str(self.scene_info['end_frame']))
        
        
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
    


