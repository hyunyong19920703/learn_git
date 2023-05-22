import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QListWidget
from PySide2 import QtWidgets, QtCore, QtGui


class DraggableLabel(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        for url in urls:
            print(url.toLocalFile())
            
class Drop_Event_layout(QtWidgets.QVBoxLayout):
    def __init__(self, parent=None):
        super().__init__()
        
        
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        for url in urls:
            print(url.toLocalFile())
            
class MyListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDragEnabled(True)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                self.addItem(url.path())
            event.accept()
        elif event.mimeData().urls() is not None:
            urls = event.mimeData().urls()
            for url in urls:
                print(url.toLocalFile())
                self.addItem(url.path())
        else:
            event.ignore()   
              

        

    
class MyListWidget_two(QListWidget):
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                self.addItem(url.path())
            event.accept()
        else:
            event.ignore()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.list_widget = MyListWidget()
        self.label = DraggableLabel("Label", self)

        self.layout = Drop_Event_layout()
        self.layout.addWidget(self.list_widget)
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)

        self.list_widget.addItem("File 1")
        self.list_widget.addItem("File 2")
        self.list_widget.addItem("File 3")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())
