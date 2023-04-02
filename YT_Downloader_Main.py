from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os
import subprocess
import shutil
from pytube import YouTube


class Ui_YouTubeDownloader(object):
    def __init__(self):
        super().__init__()
        self.destination = 'C:/Music/Download/'
        self.landing = 'C:/Music/MP3_Playlist/'
        self.backup = 'C:/Music/Backup/'

    def setupUi(self, YouTubeDownloader):
        YouTubeDownloader.setObjectName("MP3_Player")
        YouTubeDownloader.resize(446, 157)
        icon = QtGui.QIcon.fromTheme("Python")
        YouTubeDownloader.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(YouTubeDownloader)
        self.centralwidget.setObjectName("centralwidget")
        self.instructions_label = QtWidgets.QLabel(self.centralwidget)
        self.instructions_label.setGeometry(QtCore.QRect(10, 10, 400, 20))
        font = QtGui.QFont()


        font.setPointSize(14)
        self.instructions_label.setFont(font)
        self.instructions_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.instructions_label.setObjectName("instructions_label")
        self.base_address_label = QtWidgets.QLabel(self.centralwidget)
        self.base_address_label.setGeometry(QtCore.QRect(10, 40, 270, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.base_address_label.setFont(font)
        self.base_address_label.setFrameShape(QtWidgets.QFrame.Box)
        self.base_address_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.base_address_label.setObjectName("base_address_label")
        self.yt_code_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.yt_code_lineEdit.setGeometry(QtCore.QRect(285, 40, 151, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.yt_code_lineEdit.setFont(font)
        self.yt_code_lineEdit.setObjectName("yt_code_lineEdit")
        self.download_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.download_pushButton.setGeometry(QtCore.QRect(300, 80, 100, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.download_pushButton.setFont(font)
        self.download_pushButton.setObjectName("download_pushButton")
        YouTubeDownloader.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(YouTubeDownloader)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 446, 21))
        self.menubar.setObjectName("menubar")
        YouTubeDownloader.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(YouTubeDownloader)
        self.statusbar.setObjectName("statusbar")
        YouTubeDownloader.setStatusBar(self.statusbar)

        self.retranslateUi(YouTubeDownloader)
        QtCore.QMetaObject.connectSlotsByName(YouTubeDownloader)

        self.download_pushButton.clicked.connect(self.the_process)


    def retranslateUi(self, YouTubeDownloader):
        _translate = QtCore.QCoreApplication.translate
        YouTubeDownloader.setWindowTitle(_translate("MP3_Player", "You Tube Downloader"))
        self.instructions_label.setText(_translate("MP3_Player", "Enter the YouTube item code to download:"))
        self.base_address_label.setText(_translate("MP3_Player", "https://www.youtube.com/watch?v="))
        self.download_pushButton.setText(_translate("MP3_Player", "Download"))

    def no_blanks(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        # setting message for Message Box
        msg.setText("Cannot Be Blank.")

        # setting Message box window title
        msg.setWindowTitle("Invalid Information")

        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)

        # start the app
        retval = msg.exec_()

    def successful_download(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        # setting message for Message Box
        msg.setText(self.title + " has been successfully downloaded.")

        # setting Message box window title
        msg.setWindowTitle("Download Complete")

        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)

        # start the app
        retval = msg.exec_()

    def error_download(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        # setting message for Message Box
        msg.setText("Your download failed...")

        # setting Message box window title
        msg.setWindowTitle("Download Failed")

        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)

        # start the app
        retval = msg.exec_()

    def download_file(self):
        base_URL = 'https://www.youtube.com/watch?v='
        yt_link = self.yt_code_lineEdit.text()

        link = (base_URL + yt_link)
        # print(str(link))
        youtubeObject = YouTube(link)
        # extract only audio
        video = youtubeObject.streams.filter(only_audio=True).first()
        self.title = youtubeObject.title

        # download the file
        out_file = video.download(output_path=self.destination)

        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file.replace(' ', '_').replace("'", "").replace('"', '').replace(',', '').replace('&', ''))

    def convert_webm(self):
        ffmpeg_loc = 'c:/ffmpeg/'
        input_loc = self.destination
        output_loc = self.landing
        filenames = os.listdir(input_loc)
        print(filenames)
        for filename in filenames:
            print(filename)
            command = ffmpeg_loc + 'ffmpeg.exe -i ' + input_loc + filename + ' ' + output_loc + filename
            print(command)
            subprocess.run(command)
            shutil.move(self.destination + filename, self.backup)

    def the_process(self):
        try:
            if self.yt_code_lineEdit.text() == '':
                self.no_blanks()
            else:
                self.download_file()
                self.convert_webm()
                self.successful_download()
                self.yt_code_lineEdit.setText("")
        except:
            self.error_download()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    YouTubeDownloader = QtWidgets.QMainWindow()
    ui = Ui_YouTubeDownloader()
    ui.setupUi(YouTubeDownloader)
    YouTubeDownloader.show()
    sys.exit(app.exec_())
