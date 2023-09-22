import sys

from PySide6 import QtWidgets, QtCore
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtWidgets import QMainWindow, QApplication, QTableView, QMessageBox
from ui_py import login
import ora_database

class loginmainwindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=login.Ui_MainWindow()
        self.ui.setupUi(self)

        self.show()

    def log_in(self):
        orcl=ora_database.ora_database()
        u_id=self.ui.id.toPlainText()
        u_code=self.ui.pwd.toPlainText()
        res=orcl.user_login(u_id,u_code)
        if res==1:
            message_box = QMessageBox()
            message_box.setText("用户名不存在！")
            message_box.setStandardButtons(QMessageBox.Ok)
            message_box.exec()

        if res==2:
            message_box = QMessageBox()
            message_box.setText("密码错误！")
            message_box.setStandardButtons(QMessageBox.Ok)
            message_box.exec()

        if res==3:









if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = loginmainwindow()
    win.show()
    sys.exit(app.exec())
