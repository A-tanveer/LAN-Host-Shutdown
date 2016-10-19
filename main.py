import sys

from PyQt5.QtWidgets import QDialog, QApplication

import form


class MainWindow (QDialog, form.Ui_Form):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':

    app = QApplication(sys.argv)

    form = MainWindow()
    form.show()

    sys.exit(app.exec_())
