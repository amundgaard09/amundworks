
import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QSizePolicy

class ProdigyApplication(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Prodigy v.0.0.0.1")
        self.setGeometry(0, 0, 1280, 800)
        
        ### Container
        self.ApplicationContainer = QtWidgets.QWidget()
        
        #Layouts
        self.OuterLayout = QtWidgets.QVBoxLayout()
        self.InnerLayout = QtWidgets.QHBoxLayout()
        self.ApplicationContainer.setLayout(self.OuterLayout)
    
        ### Background & Central Widget
        StyleSheet = "background-color: #0a0c0e"
        self.setStyleSheet(StyleSheet)
        self.setCentralWidget(self.ApplicationContainer)
        
        ### Panel Containers
        self.LeftNavBarContainer = QtWidgets.QWidget()
        self.TopInfoBarContainer = QtWidgets.QWidget()
        self.MainAreaContainer   = QtWidgets.QWidget()
        
        self.InnerLayout.addWidget(self.TopInfoBarContainer)
        self.InnerLayout.addWidget(self.MainAreaContainer)
        
        self.OuterLayout.addWidget(self.LeftNavBarContainer)
        self.OuterLayout.addWidget(self.InnerLayout)
        
        
        
        
        
        
        
    
    @QtCore.Slot()
    def place(self) -> None:
        pass
             
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    ProdigyInstance = ProdigyApplication()
    ProdigyInstance.show()

    sys.exit(app.exec())