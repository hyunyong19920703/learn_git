import typing
from PySide2 import QtCore
import PySide2.QtCore

class Make_Item(object):
    
    def __init__(self, data_dict) -> None:
        self.name = data_dict.get('name')
        self.type = data_dict.get('type')


class Camera_Model(QtCore.QAbstractTableModel):
    HORIZONTAL_HEADERS = ['name', 'type', 'btn', 'comboBox', 'checkBox']
    
    def __init__(self, row_datas=None, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        
        self.entri_data = list()
        for data_dict in row_datas:
            item = Make_Item(data_dict=data_dict)
            self.entri_data.append(item)
            
    def rowCount(self, parent):
        return len(self.entri_data)
    
    def columnCount(self, parent):
        return len(self.HORIZONTAL_HEADERS)
    
    def headerData(self, row, orientation, role):
        if orientation == QtCore.Qt.Horizontal:
            if role == QtCore.Qt.DisplayRole:
                return self.HORIZONTAL_HEADERS[row]
        elif orientation == QtCore.Qt.Vertical:
            if role == QtCore.Qt.DisplayRole:
                return QtCore.QAbstractTableModel.headerData(self, row, orientation, role)
        
    def data(self, index, role):
        row = index.row()
        column = index.column()
        item = self.entri_data[row]
        
        if role == QtCore.Qt.DisplayRole:
            if column == 0:
                return item.name
            elif column == 1:
                return item.type
            
    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable
            