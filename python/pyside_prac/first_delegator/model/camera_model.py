from PySide2 import QtCore, QtGui, QtWidgets
from functools import partial


class Make_Item(object):
    
    def __init__(self, data_dict) -> None:
        self.name = data_dict.get('name')
        self.type = data_dict.get('type')
        self.checked = True
        self.boxes_value = data_dict.get('boxes_value')
        self.item = data_dict
        
    def setChecked(self, checked=True):
        self.checked = checked
        


class Camera_Model(QtCore.QAbstractTableModel):
    HORIZONTAL_HEADERS = ['name', 'type', 'boxes', 'btn', 'comboBox', 'checkBox']
    
    def __init__(self, row_datas=None, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self.img_path = 'C:\\Users\\user\\Desktop\\python_project\\python\\pyside_prac\\first_delegator\\icon'
        self.checked_icon = f"{self.img_path}\\check.png"
        self.unchecked_icon = f"{self.img_path}\\uncheck.png"    
        
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
        elif role == QtCore.Qt.CheckStateRole:
            if column == 1:
                if item.checked == True:
                    return QtCore.Qt.Checked
                else:
                    return QtCore.Qt.Unchecked  
                
        elif role == QtCore.Qt.DecorationRole:
            if column == 1:
                if item.checked == True:
                    return QtGui.QPixmap(self.checked_icon).scaledToHeight(30)
                else:
                    return QtGui.QPixmap(self.unchecked_icon).scaledToHeight(30)
        
        elif role == QtCore.Qt.UserRole:
            return item

    def setData(self, index, value, role):
        if index.isValid():
            row_data = self.entri_data[index.row()]
            
            if role == QtCore.Qt.CheckStateRole:                
                row_data.setChecked(checked=not row_data.checked)
                print(row_data.checked)
                return True
            
            elif role == QtCore.Qt.UserRole:    
                # value is QCheckBox
                name = value.text()
                state = value.isChecked()                
                row_data.boxes_value[name] = state
                
                if value.isChecked():
                    value.setIcon(QtGui.QIcon(self.checked_icon))
                else:
                    value.setIcon(QtGui.QIcon(self.unchecked_icon))
                
                return True  
        return False  
            
    def flags(self, index):
        return QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable


class Prac_Delegator(QtWidgets.QItemDelegate):
    box_clicked = QtCore.Signal(object, object, object)
    
    def __init__(self, parent=None):
        QtWidgets.QItemDelegate.__init__(self, parent) 
        self.img_path = 'C:\\Users\\user\\Desktop\\python_project\\python\\pyside_prac\\first_delegator\\icon'
        self.checked_icon = f"{self.img_path}\\check.png"
        self.unchecked_icon = f"{self.img_path}\\uncheck.png"      
        
    def createEditor(self, parent, option, index):
        column = index.column()
        row_data = index.data(QtCore.Qt.UserRole)
        
        if column == 2:
            editor = QtWidgets.QWidget(parent)
            layout = QtWidgets.QVBoxLayout(editor)
            for name, value in row_data.boxes_value.items():                
                check_box = QtWidgets.QCheckBox()
                check_box.setText(name)
                check_box.setChecked(value) 
                check_box.setIcon(QtGui.QIcon(self.checked_icon))     
                check_box.stateChanged.connect(partial(self.checkbox_state_changed, index, check_box))
                layout.addWidget(check_box)
                
            return editor
                
                
    def checkbox_state_changed(self, index, check_box, state):
        self.box_clicked.emit(index, check_box, state)
        
    