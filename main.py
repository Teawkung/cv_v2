from PyQt5 import QtWidgets,uic
import asyncio
from face_rec import start_record
app=QtWidgets.QApplication([])

call = uic.loadUi("MainUI.ui")
call.pushButton_2.clicked.connect(start_record)



call.show()
app.exec()
