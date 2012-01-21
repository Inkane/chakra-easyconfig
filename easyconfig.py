import sys
import os

import pacman_wrapper as chakra_tool

from PyQt4 import QtCore,  QtGui
from Ui_chakrafastconfig import Ui_MainWindow as Ui_fastconfig

class StartQT4(QtGui.QMainWindow):
    
    def __init__(self,  parent=None):
        chakra_tool.backup_configuration_file() # make a backup of pacman.conf
        QtGui.QWidget.__init__(self,  parent)
        self.ui = Ui_fastconfig()
        self.ui.setupUi(self)
        #  connecting signals with slots
        QtCore.QObject.connect(self.ui.pushButton_codec,  QtCore.SIGNAL("clicked()"),  self.handle_codecs)
        QtCore.QObject.connect(self.ui.pushButton_locale,  QtCore.SIGNAL("clicked()"),  self.handle_locale)
        QtCore.QObject.connect(self.ui.pushButton_fonts,  QtCore.SIGNAL("clicked()"),  self.handle_fonts)
        QtCore.QObject.connect(self.ui.pushButton_repo,  QtCore.SIGNAL("clicked()"),  self.handle_repo)       

    def  handle_codecs(self):
        print self.ui.checkBox_codec.isChecked()
        if self.ui.checkBox_flash.isChecked():
            chakra_tool.install("flashplugin")
    
    def handle_locale(self):
        pass
        
    def handle_fonts(self):
        if self.ui.checkBox_ubuntu.isChecked():
            chakra_tool.install("ttf-ubuntu-font")
        if self.ui.checkBox_oxygen.isChecked():
            #chakra_tool.install("") Which font?
            pass
        if self.ui.checkBox_ms.isChecked():
            chakra_tool.install("ttf-ms-fonts")
        
    def handle_repo(self):
        if self.ui.checkBox_ccr.isChecked():
            chakra_tool.install("base-devel")
            chakra_tool.install("ccr")
        # change /etc/pacman.conf
        if self.ui.checkBox_testing.isChecked():
            chakra_tool.pac_conf_edit("testing")
        else:
            chakra_tool.pac_conf_edit("testing",  False)
        if self.ui.checkBox_unstable.isChecked():
            chakra_tool.pac_conf_edit("staging")
        else:
            chakra_tool.pac_conf_edit("staging",  False)
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
