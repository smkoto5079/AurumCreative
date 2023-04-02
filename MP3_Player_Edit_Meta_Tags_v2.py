from PyQt5 import QtCore, QtGui, QtWidgets
from mutagen.mp3 import EasyMP3
import os


class Ui_Edit_Tags(object):
    def __init__(self):
        self.update_path = ''

    def setupUi(self, Edit_Tags):
        Edit_Tags.setObjectName("MainWindow")
        Edit_Tags.resize(444, 249)
        self.centralwidget = QtWidgets.QWidget(Edit_Tags)
        self.centralwidget.setObjectName("centralwidget")
        self.title_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.title_lineEdit.setGeometry(QtCore.QRect(110, 50, 311, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.title_lineEdit.setFont(font)
        self.title_lineEdit.setObjectName("title_lineEdit")
        self.artist_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.artist_lineEdit.setGeometry(QtCore.QRect(110, 90, 311, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.artist_lineEdit.setFont(font)
        self.artist_lineEdit.setObjectName("artist_lineEdit")
        self.album_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.album_lineEdit.setGeometry(QtCore.QRect(110, 130, 311, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.album_lineEdit.setFont(font)
        self.album_lineEdit.setObjectName("album_lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.song_to_edit_label = QtWidgets.QLabel(self.centralwidget)
        self.song_to_edit_label.setGeometry(QtCore.QRect(16, 10, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.song_to_edit_label.setFont(font)
        self.song_to_edit_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.song_to_edit_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.song_to_edit_label.setText("")
        self.song_to_edit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.song_to_edit_label.setObjectName("song_to_edit_label")
        self.update_button = QtWidgets.QPushButton(self.centralwidget)
        self.update_button.setGeometry(QtCore.QRect(200, 170, 75, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.update_button.setFont(font)
        self.update_button.setObjectName("update_button")

        Edit_Tags.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Edit_Tags)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 444, 21))
        self.menubar.setObjectName("menubar")
        Edit_Tags.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Edit_Tags)
        self.statusbar.setObjectName("statusbar")
        Edit_Tags.setStatusBar(self.statusbar)

        self.retranslateUi(Edit_Tags)
        QtCore.QMetaObject.connectSlotsByName(Edit_Tags)

        self.update_button.clicked.connect(self.update_data)
        self.update_button.clicked.connect(Edit_Tags.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Song Title"))
        self.label_2.setText(_translate("MainWindow", "Artist"))
        self.label_3.setText(_translate("MainWindow", "Album"))
        self.update_button.setText(_translate("MainWindow", "Update"))
        # self.cancel_button.setText(_translate("MainWindow", "Cancel"))

    def display_song_data(self, path, song_label, title, artist, album):
        self.update_path = path
        self.song_to_edit_label.setText(song_label)
        self.title_lineEdit.setText(title[0])
        self.artist_lineEdit.setText(artist[0])
        self.album_lineEdit.setText(album[0])

    def update_data(self):
        file_name = self.update_path + self.song_to_edit_label.text() + '.mp3'
        tags = EasyMP3(file_name)
        tags["title"] = self.title_lineEdit.text()
        tags["artist"] = self.artist_lineEdit.text()
        tags["album"] = self.album_lineEdit.text()
        tags.save()

        old_filename = file_name
        new_filename = self.update_path + self.title_lineEdit.text() + '.mp3'
        os.rename(old_filename, new_filename)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Edit_Tags()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
