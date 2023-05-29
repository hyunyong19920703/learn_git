import typing
from PySide2 import QtCore, QtGui
import PySide2.QtCore

HORIZONTAL_HEADERS = ['Check object']


class Make_Tree_Model(object):
    def __init__(self, row_data=None, p_row=None, parentItem=None):
        
        self.item = row_data
        self.p_row = p_row
        self.parentItem = parentItem
        self.childItems = list()
        self.checked = True
        
    def appendChild(self, item):
        self.childItems.append(item)
        
    def child(self, row):
        return self.childItems[row]
    
    def childCount(self):
        return len(self.childItems)
    
    def columnCount(self):
        return len(HORIZONTAL_HEADERS)
    
    def data(self, column):
        if column == 0:
            if self.item is None:
                return HORIZONTAL_HEADERS
            else:
                return self.item
        else:
            return None
    
    def parent(self):
        return self.parentItem
    
    def row(self):
        if self.parentItem:
            return self.parentItem.childItems.index(self)
        return 0
    
    @property
    def is_checked(self):
        return self.checked
    
    def set_checked(self, checked=True):
        self.checked = bool(checked)
        


class Selected_Asset_Model(QtCore.QAbstractItemModel):
    def __init__(self, row_datas=None, parent=None):
        super(Selected_Asset_Model, self).__init__(parent)
        
        self.row_datas = row_datas
        self.rootItem = Make_Tree_Model(None, None, None)
        self.parents = {0: self.rootItem}
        self.set_model_data()
        
    def set_model_data(self):
        
        for key, value in self.row_datas.items():
            namespace = key
            object_list = value
            
            new_parent = Make_Tree_Model(row_data=namespace, p_row=1, parentItem=self.rootItem)
            self.rootItem.appendChild(new_parent)
            
            for row_item in object_list:
                new_item = Make_Tree_Model(row_data=row_item, p_row=2, parentItem=new_parent)
                new_parent.appendChild(new_item)
                
    def data(self, index, role):
        
        row = index.row()
        column = index.column()
        item = index.internalPointer()
        
        if role == QtCore.Qt.DisplayRole:
            return item.data(column)
        
        elif role == QtCore.Qt.CheckStateRole:
            if item.p_row == 2:
                if item.checked is True:
                    return QtCore.Qt.Checked
                else:
                    return QtCore.Qt.Unchecked
        elif role == QtCore.Qt.UserRole:
            return item
                
    def setData(self, index, value, role):
        if index.isValid():
            if role == QtCore.Qt.CheckStateRole:
                row_data = index.internalPointer()
                row_data.set_checked(not row_data.is_checked)
                return True
        return False
        
    def rowCount(self, parent=QtCore.QModelIndex()):
        
        if parent.column() > 0:
            return 0
        if not parent.isValid():
            parent_Item = self.rootItem
        else:
            parent_Item = parent.internalPointer()
        return parent_Item.childCount()
    
    def index(self, row, column, parent):
        
        if not self.hasIndex(row, column, parent):
            return QtCore.QModelIndex()
        
        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()
            
        childItem = parentItem.childItems[row]
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QtCore.QModelIndex()
        
    def parent(self, index):
        
        if not index.isValid():
            return QtCore.QModelIndex()
        
        childItem = index.internalPointer()
        
        if not childItem:
            return QtCore.QModelIndex()
        
        parentItem = childItem.parent()
        
        if parentItem == self.rootItem:
            return QtCore.QModelIndex()
        
        return self.createIndex(parentItem.row(), 0, parentItem)
    
    def columnCount(self, parent=None):
        return len(HORIZONTAL_HEADERS)
    
    def headerData(self, column, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return HORIZONTAL_HEADERS[column]
        return None
    
    def removeRows(self, position, rows, parent=QtCore.QModelIndex()):
        start, end = position, rows
        self.beginRemoveRows(parent, start, end)
        del self._data[start:end + 1]
        self.endRemoveRows()
        return True
    
    def flags(self, index):
        row_data = index.internalPointer()
        column = index.column()
        if column == 0:
            if row_data.p_row == 2:
                return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsUserCheckable
            else:
                return QtCore.Qt.ItemIsEnabled
            
        