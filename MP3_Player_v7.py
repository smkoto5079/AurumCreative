import shutil
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget
from MP3_Player.Versions.YT_Downloader_Main import Ui_YouTubeDownloader
from Edit_Meta_Tags_v2 import Ui_Edit_Tags
from mutagen.mp3 import MP3
from mutagen.mp3 import EasyMP3
import pygame
import time
from tinytag import TinyTag
import os
from PyQt5.QtCore import *
import random

# Initialize PyGame Mixer
pygame.mixer.init()

path = 'C:/Music/MP3_Playlist/'
mp3_path = path
filenames = os.listdir(path)

initial_playlist_list = []
for file in filenames:
    initial_playlist_list.append(file)


class Ui_MainWindow(object):
    def __init__(self):
        self.count = 0
        self.start = False
        self.is_stopped = False
        self.is_paused = False
        self.song_length = 0
        self.is_playing = False
        self.shuffle = False

        self.timer = QTimer()
        self.timer.timeout.connect(self.showTime)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(355, 630)
        font10 = QtGui.QFont()
        font10.setPointSize(10)
        font12 = QtGui.QFont()
        font12.setPointSize(12)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.song_label = QtWidgets.QLabel(self.centralwidget)
        self.song_label.setGeometry(QtCore.QRect(70, 450, 191, 25))
        self.song_label.setToolTipDuration(0)
        self.song_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.song_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.song_label.setMidLineWidth(0)
        self.song_label.setText("")
        self.song_label.setFont(font10)
        self.song_label.setObjectName("song_label")
        self.artist_label = QtWidgets.QLabel(self.centralwidget)
        self.artist_label.setGeometry(QtCore.QRect(70, 480, 191, 25))
        self.artist_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.artist_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.artist_label.setText("")
        self.artist_label.setFont(font10)
        self.artist_label.setObjectName("artist_label")
        self.album_label = QtWidgets.QLabel(self.centralwidget)
        self.album_label.setGeometry(QtCore.QRect(70, 510, 191, 25))
        self.album_label.setFrameShape(QtWidgets.QFrame.Panel)
        self.album_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.album_label.setText("")
        self.album_label.setFont(font10)
        self.album_label.setObjectName("album_label")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 380, 331, 25))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.divider_line = QtWidgets.QFrame(self.centralwidget)
        self.divider_line.setGeometry(QtCore.QRect(10, 430, 331, 20))
        self.divider_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.divider_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.divider_line.setObjectName("divider_line")
        self.song_length_start_label = QtWidgets.QLabel(self.centralwidget)
        self.song_length_start_label.setGeometry(QtCore.QRect(110, 400, 70, 30))
        self.song_length_start_label.setFont(font12)
        self.song_length_start_label.setAlignment(QtCore.Qt.AlignCenter)
        self.song_length_start_label.setObjectName("song_length_start_label")
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setGeometry(QtCore.QRect(270, 440, 70, 70))
        self.dial.setRange(0, 100)
        self.dial.setNotchesVisible(True)
        self.dial.setObjectName("dial")
        self.volume_label = QtWidgets.QLabel(self.centralwidget)
        self.volume_label.setGeometry(QtCore.QRect(270, 510, 70, 25))
        self.volume_label.setFont(font12)
        self.volume_label.setFrameShape(QtWidgets.QFrame.Box)
        self.volume_label.setAlignment(QtCore.Qt.AlignCenter)
        self.volume_label.setObjectName("volume_label")
        self.button_play = QtWidgets.QPushButton(self.centralwidget)
        self.button_play.setGeometry(QtCore.QRect(30, 340, 50, 30))
        self.button_play.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.button_play.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Icons/control.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_play.setIcon(icon)
        self.button_play.setObjectName("button_play")
        self.button_pause = QtWidgets.QPushButton(self.centralwidget)
        self.button_pause.setGeometry(QtCore.QRect(90, 340, 50, 30))
        self.button_pause.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/Icons/control-pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_pause.setIcon(icon1)
        self.button_pause.setObjectName("button_pause")
        self.button_stop = QtWidgets.QPushButton(self.centralwidget)
        self.button_stop.setGeometry(QtCore.QRect(150, 340, 50, 30))
        self.button_stop.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/Icons/control-stop-square.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_stop.setIcon(icon2)
        self.button_stop.setObjectName("button_stop")
        self.button_back = QtWidgets.QPushButton(self.centralwidget)
        self.button_back.setGeometry(QtCore.QRect(210, 340, 50, 30))
        self.button_back.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/Icons/arrow-180.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_back.setIcon(icon3)
        self.button_back.setObjectName("button_back")
        self.button_forward = QtWidgets.QPushButton(self.centralwidget)
        self.button_forward.setGeometry(QtCore.QRect(270, 340, 50, 30))
        self.button_forward.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/Icons/arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_forward.setIcon(icon4)
        self.button_forward.setObjectName("button_forward")
        self.song_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.song_label_2.setGeometry(QtCore.QRect(10, 450, 51, 25))
        self.song_label_2.setToolTipDuration(0)
        self.song_label_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.song_label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.song_label_2.setMidLineWidth(0)
        self.song_label_2.setFont(font10)
        self.song_label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.song_label_2.setObjectName("song_label_2")
        self.song_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.song_label_3.setGeometry(QtCore.QRect(10, 480, 51, 25))
        self.song_label_3.setToolTipDuration(0)
        self.song_label_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.song_label_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.song_label_3.setMidLineWidth(0)
        self.song_label_3.setFont(font10)
        self.song_label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.song_label_3.setObjectName("song_label_3")
        self.song_label_4 = QtWidgets.QLabel(self.centralwidget)
        self.song_label_4.setGeometry(QtCore.QRect(10, 510, 51, 25))
        self.song_label_4.setToolTipDuration(0)
        self.song_label_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.song_label_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.song_label_4.setMidLineWidth(0)
        self.song_label_4.setFont(font10)
        self.song_label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.song_label_4.setObjectName("song_label_4")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 10, 311, 321))
        self.listWidget.setObjectName("listWidget")
        self.song_length_end_label = QtWidgets.QLabel(self.centralwidget)
        self.song_length_end_label.setGeometry(QtCore.QRect(180, 400, 70, 30))
        self.song_length_end_label.setFont(font12)
        self.song_length_end_label.setAlignment(QtCore.Qt.AlignCenter)
        self.song_length_end_label.setObjectName("song_length_end_label")
        self.song_length_slash_label = QtWidgets.QLabel(self.centralwidget)
        self.song_length_slash_label.setGeometry(QtCore.QRect(170, 400, 20, 30))
        self.song_length_slash_label.setFont(font12)
        self.song_length_slash_label.setAlignment(QtCore.Qt.AlignCenter)
        self.song_length_slash_label.setObjectName("song_length_slash_label")
        self.shuffle_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.shuffle_checkbox.setGeometry(QtCore.QRect(10, 550, 91, 31))
        self.shuffle_checkbox.setChecked(True)
        self.shuffle_checkbox.setObjectName("shuffle_checkbox")
        self.repeat_song_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.repeat_song_checkbox.setGeometry(QtCore.QRect(140, 550, 91, 31))
        self.repeat_song_checkbox.setObjectName("repeat_song_checkbox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 355, 22))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionOptions = QtWidgets.QAction(MainWindow)
        self.actionOptions.setObjectName("actionOptions")

        self.actionAdd = QtWidgets.QAction(MainWindow)
        self.actionAdd.setObjectName("actionAdd")

        self.actionChange = QtWidgets.QAction(MainWindow)
        self.actionChange.setObjectName("actionChange")

        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")

        self.actionRefresh = QtWidgets.QAction(MainWindow)
        self.actionRefresh.setObjectName("actionRefresh")

        # self.actionDownload_from_YT = QtWidgets.QAction(MainWindow)
        # self.actionDownload_from_YT.setObjectName("actionDownload_from_YT")

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        self.actionEdit = QtWidgets.QAction(MainWindow)
        self.actionEdit.setObjectName("actionEdit")

        self.menuOptions.addAction(self.actionAdd)
        self.menuOptions.addAction(self.actionEdit)
        self.menuOptions.addAction(self.actionDelete)
        self.menuOptions.addAction(self.actionRefresh)
        self.menuOptions.addSeparator()
        # self.menuOptions.addAction(self.actionDownload_from_YT)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionExit)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.refresh_playlist()
        self.volume_label.setText('25')
        self.dial.setValue(25)
        self.actionRefresh.triggered.connect(self.refresh_playlist)
        self.actionDelete.triggered.connect(self.delete_song)
        self.actionAdd.triggered.connect(self.openFileNamesDialog)
        self.actionEdit.triggered.connect(self.update_meta_tags)
        # self.actionDownload_from_YT.triggered.connect(self.download_from_yt_window)
        self.listWidget.itemClicked.connect(self.get_the_selected_song)
        self.listWidget.itemDoubleClicked.connect(self.play_song)
        self.button_play.clicked.connect(self.play_song)
        self.button_stop.clicked.connect(self.stop_song)
        self.button_pause.clicked.connect(self.pause_song)
        # self.button_replay.clicked.connect(self.play_song)
        self.button_forward.clicked.connect(self.next_song)
        self.button_back.clicked.connect(self.prev_song)
        self.dial.valueChanged.connect(self.volume_control)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MP3 Player"))
        self.song_length_start_label.setText(_translate("MainWindow", "00:00"))
        self.volume_label.setText(_translate("MainWindow", "0"))
        self.song_label_2.setText(_translate("MainWindow", "Song"))
        self.song_label_3.setText(_translate("MainWindow", "Artist"))
        self.song_label_4.setText(_translate("MainWindow", "Album"))
        self.song_length_end_label.setText(_translate("MainWindow", "00:00"))
        self.song_length_slash_label.setText(_translate("MainWindow", "/"))
        self.shuffle_checkbox.setText(_translate("MainWindow", "Shuffle"))
        self.repeat_song_checkbox.setText(_translate("MainWindow", "Repeat"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionOptions.setText(_translate("MainWindow", "Options"))
        self.actionAdd.setText(_translate("MainWindow", "Add"))
        self.actionChange.setText(_translate("MainWindow", "Change"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionRefresh.setText(_translate("MainWindow", "Refresh"))
        # self.actionDownload_from_YT.setText(_translate("MainWindow", "Download from YT"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionEdit.setText(_translate("MainWindow", "Edit"))

    def openFileNamesDialog(self):
        self.open_file = App()
        self.open_file.openFileNamesDialog()

        self.refresh_playlist()

    def refresh_playlist(self):
        self.stop_song()
        self.listWidget.clearSelection()
        self.listWidget.setCurrentRow(0)

        # Get the file path to where the music is stored
        path = 'C:/Music/MP3_Playlist/'
        # path = os.getcwd() + '/MP3/MP3_Playlist/'
        refresh_filenames = os.listdir(path)
        self.listWidget.clear()

        self.refresh_playlist_list = []
        for refresh_file in refresh_filenames:
            self.refresh_playlist_list.append(refresh_file)
            self.listWidget.addItem(refresh_file[:-4])

    def delete_song(self):
        # path = os.getcwd() + '/MP3/MP3_Playlist/'
        path = 'C:/Music/MP3_Playlist/'
        delete_filenames = os.listdir(path)

        self.delete_playlist_list = []
        for delete_file in delete_filenames:
            self.delete_playlist_list.append(delete_file)

        del_song = f'{path}' + self.delete_playlist_list[self.listWidget.currentRow()]

        if os.path.isfile(del_song):
            os.remove(f'{del_song}')
        else:  ## Show an error ##
            print("Error: %s file not found" % del_song)

        self.refresh_playlist()

    def showTime(self):
        if self.start:
            current_time = pygame.mixer.music.get_pos() / 1000
            converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))
            self.song_length_start_label.setText(converted_current_time)
            self.song_length = int(self.song_mut.info.length)

            self.horizontalSlider.setMinimum(0)
            # print(self.song_length)
            self.horizontalSlider.setMaximum(self.song_length)
            self.horizontalSlider.setValue(int(current_time))

            if current_time < 0:
                if self.shuffle_checkbox.isChecked() and self.repeat_song_checkbox.isChecked():
                    self.shuffle_songs()
                    self.play_song()
                elif self.shuffle_checkbox.isChecked():
                    self.shuffle_songs()
                    self.play_song()
                elif self.repeat_song_checkbox.isChecked():
                    self.play_song()
                else:
                    self.next_song()

    def shuffle_songs(self):
        num = random.randint(1, len(self.refresh_playlist_list)) - 1
        self.listWidget.setCurrentRow(num)

    def startTimer(self):
        self.timer.start(1000)

    def stopTimer(self):
        self.timer.stop()

    def get_the_selected_song(self):
        if self.is_playing:
            return
        else:
            # Find the currently selected file in the playlist
            audio_file_info = TinyTag.get(path + str(self.refresh_playlist_list[self.listWidget.currentRow()]))
            self.artist_label.setText(audio_file_info.artist)
            self.song_label.setText(str(self.refresh_playlist_list[self.listWidget.currentRow()][:-4]))
            self.album_label.setText(audio_file_info.album)
            self.song_length = self.get_song_length()
            self.song_length_end_label.setText(self.song_length)

    def play_song(self):
        self.is_playing = False
        self.get_the_selected_song()
        self.song_length_start_label.setText('00:00')
        self.is_playing = True
        self.is_stopped = False
        self.start = True
        self.count = 0

        song = f'{path}' + self.refresh_playlist_list[self.listWidget.currentRow()]

        pygame.mixer.music.load(str(song))
        pygame.mixer.music.play()
        self.startTimer()

    def stop_song(self):
        self.start = False
        self.count = 0
        self.is_playing = False
        pygame.mixer.music.stop()
        self.stopTimer()

    def pause_song(self):
        if self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
            self.is_playing = True
            self.startTimer()
        else:
            pygame.mixer.music.pause()
            self.is_paused = True
            self.is_playing = True
            self.stopTimer()

    def next_song(self):
        self.is_playing = True
        self.is_paused = False
        self.start = True
        self.count = 0

        if self.shuffle_checkbox.isChecked():
            self.shuffle_songs()
        else:
            current_song = self.listWidget.currentRow()
            new_song = current_song + 1

            if new_song > len(self.refresh_playlist_list) - 1:
                current_song = 0
                song = f'{path}' + self.refresh_playlist_list[current_song]
                self.listWidget.setCurrentRow(current_song)
            else:
                song = f'{path}' + self.refresh_playlist_list[new_song]
                self.listWidget.setCurrentRow(new_song)

        # # Find the currently selected file in the playlist
        # # audio_file_info = TinyTag.get(song)
        # self.get_the_selected_song()
        self.play_song()

    def prev_song(self):
        self.is_playing = True
        self.is_paused = False
        self.start = True
        self.count = 0

        current_song = self.listWidget.currentRow()
        new_song = current_song - 1

        if self.listWidget.currentRow() - 1 < 0:
            song = f'{path}' + self.refresh_playlist_list[current_song]
            self.listWidget.setCurrentRow(current_song)
        else:
            song = f'{path}' + self.refresh_playlist_list[new_song]
            self.listWidget.setCurrentRow(new_song)

        # Find the currently selected file in the playlist
        # audio_file_info = TinyTag.get(song)
        # self.get_the_selected_song()
        self.play_song()

    def volume_control(self):
        # Grab the Current dial position
        self.dial.value()
        value = self.dial.value()
        pygame.mixer.music.set_volume(value/100)
        # Set label text
        self.volume_label.setText(f'{str(value)}')

    def get_song_length(self):
        # Load song and get song length with Mutagen
        self.song_mut = MP3(f'{path}' + self.refresh_playlist_list[self.listWidget.currentRow()])

        # Convert to our time format
        self.current_song_length = time.strftime('%M:%S', time.gmtime(self.song_mut.info.length))
        return self.current_song_length

    def send_values_to_meta(self):
        current_song_title = self.listWidget.currentItem().text()
        current_song_name = path + self.listWidget.currentItem().text() + '.mp3'

        tags_blank = EasyMP3(current_song_name)
        tags_blank['title'] = current_song_title
        tags_blank.save()

        if self.artist_label.text() == '':
            tags_blank['artist'] = 'Unknown Artist'
            tags_blank.save()
        if self.album_label.text() == '':
            tags_blank['album'] = 'Unknown Album'
            tags_blank.save()

        tags = EasyMP3(path + self.listWidget.currentItem().text() + '.mp3')

        mp3_title = tags["title"]
        mp3_artist = tags["artist"]
        mp3_album = tags['album']

        self.meta_tags.display_song_data(path, current_song_title, mp3_title, mp3_artist, mp3_album)

    # def download_from_yt_window(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.yt = Ui_YouTubeDownloader()
    #     self.yt.setupUi(self.window)
    #     self.window.show()

    def update_meta_tags(self):
        self.window = QtWidgets.QMainWindow()
        self.meta_tags = Ui_Edit_Tags()
        self.meta_tags.setupUi(self.window)
        self.window.show()
        self.send_values_to_meta()
        self.refresh_playlist()


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480

    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "All Files (*);;Python Files (*.py)", options=options)

        if files:
            for copy_file in files:
                source = copy_file
                destination = mp3_path
                shutil.copy(source, destination)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
