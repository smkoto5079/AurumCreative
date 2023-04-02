from PyQt5 import QtCore, QtGui, QtWidgets
from googletrans import Translator
from TranslatR_Validations import Validations
from TranslatR_Sounds import Sounds
from functools import partial

button = 'Icons/speaker-volume.png'
size = 12


class Ui_Add_MainWindow(object):
    def __init__(self):
        self.last_item = None
        self.sound_instance = Sounds()
        self.validation_instance = Validations()

    def setupUi(self, Add_MainWindow):
        Add_MainWindow.setObjectName("Add_MainWindow")
        Add_MainWindow.resize(421, 591)
        Add_MainWindow.setWindowTitle("Add an Entry")
        self.centralwidget = QtWidgets.QWidget(Add_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.new_entry_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.new_entry_textEdit.setGeometry(QtCore.QRect(110, 60, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(size)
        self.new_entry_textEdit.setFont(font)
        self.new_entry_textEdit.setObjectName("new_entry_textEdit")
        self.italian_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.italian_textEdit.setGeometry(QtCore.QRect(110, 360, 251, 51))
        self.italian_textEdit.setFont(font)
        self.italian_textEdit.setObjectName("italian_textEdit")
        self.add_sound_french_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_sound_french_button.setGeometry(QtCore.QRect(370, 300, 40, 51))
        self.add_sound_french_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(button), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_sound_french_button.setIcon(icon)
        self.add_sound_french_button.setObjectName("add_sound_french_button")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 300, 81, 51))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 180, 81, 51))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.german_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.german_textEdit.setGeometry(QtCore.QRect(110, 420, 251, 51))
        self.german_textEdit.setFont(font)
        self.german_textEdit.setObjectName("german_textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 240, 81, 51))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.english_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.english_textEdit.setGeometry(QtCore.QRect(110, 180, 251, 51))
        self.english_textEdit.setFont(font)
        self.english_textEdit.setObjectName("english_textEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 360, 81, 51))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.add_sound_english_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_sound_english_button.setGeometry(QtCore.QRect(370, 180, 40, 51))
        self.add_sound_english_button.setText("")
        self.add_sound_english_button.setIcon(icon)
        self.add_sound_english_button.setObjectName("add_sound_english_button")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 420, 81, 51))
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.add_sound_italian_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_sound_italian_button.setGeometry(QtCore.QRect(370, 360, 40, 51))
        self.add_sound_italian_button.setText("")
        self.add_sound_italian_button.setIcon(icon)
        self.add_sound_italian_button.setObjectName("add_sound_italian_button")
        self.french_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.french_textEdit.setGeometry(QtCore.QRect(110, 300, 251, 51))
        self.french_textEdit.setFont(font)
        self.french_textEdit.setObjectName("french_textEdit")
        self.add_sound_german_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_sound_german_button.setGeometry(QtCore.QRect(370, 420, 40, 51))
        self.add_sound_german_button.setText("")
        self.add_sound_german_button.setIcon(icon)
        self.add_sound_german_button.setObjectName("add_sound_german_button")
        self.spanish_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.spanish_textEdit.setGeometry(QtCore.QRect(110, 240, 251, 51))
        self.spanish_textEdit.setFont(font)
        self.spanish_textEdit.setObjectName("spanish_textEdit")
        self.add_sound_spanish_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_sound_spanish_button.setGeometry(QtCore.QRect(370, 240, 40, 51))
        self.add_sound_spanish_button.setText("")
        self.add_sound_spanish_button.setIcon(icon)
        self.add_sound_spanish_button.setObjectName("add_sound_spanish_button")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 160, 401, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.new_entry_language_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.new_entry_language_combobox.setGeometry(QtCore.QRect(110, 130, 141, 31))
        self.new_entry_language_combobox.setFont(font)
        self.new_entry_language_combobox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.new_entry_language_combobox.setEditable(True)
        self.new_entry_language_combobox.setObjectName("new_entry_language_combobox")
        self.new_entry_language_combobox.addItem("")
        self.new_entry_language_combobox.addItem("")
        self.new_entry_language_combobox.addItem("")
        self.new_entry_language_combobox.addItem("")
        self.new_entry_language_combobox.addItem("")
        self.new_entry_language_combobox.addItem("")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 130, 81, 31))
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 65, 81, 51))
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(10, 40, 401, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.get_translations_button = QtWidgets.QPushButton(self.centralwidget)
        self.get_translations_button.setGeometry(QtCore.QRect(260, 130, 81, 31))
        self.get_translations_button.setObjectName("get_translations_button")
        self.portuguese_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.portuguese_textEdit.setGeometry(QtCore.QRect(110, 480, 251, 51))
        self.portuguese_textEdit.setFont(font)
        self.portuguese_textEdit.setObjectName("portuguese_textEdit")
        self.add_sound_portuguese_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_sound_portuguese_button.setGeometry(QtCore.QRect(370, 480, 40, 51))
        self.add_sound_portuguese_button.setText("")
        self.add_sound_portuguese_button.setIcon(icon)
        self.add_sound_portuguese_button.setObjectName("add_sound_portuguese_button")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 480, 81, 51))
        self.label_11.setFont(font)
        self.label_11.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.label_11.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_11.setObjectName("label_11")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(350, 130, 61, 31))
        self.clear_button.setObjectName("clear_button")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 10, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(True)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        Add_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Add_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 421, 21))
        self.menubar.setObjectName("menubar")
        Add_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Add_MainWindow)
        self.statusbar.setObjectName("statusbar")
        Add_MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(Add_MainWindow)
        self.new_entry_language_combobox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Add_MainWindow)

        self.add_sound_english_button.clicked.connect(partial(self.get_pronunciation, 1))
        self.add_sound_spanish_button.clicked.connect(partial(self.get_pronunciation, 2))
        self.add_sound_french_button.clicked.connect(partial(self.get_pronunciation, 3))
        self.add_sound_italian_button.clicked.connect(partial(self.get_pronunciation, 4))
        self.add_sound_german_button.clicked.connect(partial(self.get_pronunciation, 5))
        self.add_sound_portuguese_button.clicked.connect(partial(self.get_pronunciation, 6))
        self.get_translations_button.clicked.connect(self.get_translations)
        self.clear_button.clicked.connect(self.clear_entry)

    def retranslateUi(self, Add_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("Add_MainWindow", "French"))
        self.label.setText(_translate("Add_MainWindow", "English"))
        self.label_2.setText(_translate("Add_MainWindow", "Spanish"))
        self.label_4.setText(_translate("Add_MainWindow", "Italian"))
        self.label_5.setText(_translate("Add_MainWindow", "German"))
        self.label_6.setText(_translate("Add_MainWindow", "TranslatR"))
        self.new_entry_language_combobox.setCurrentText(_translate("Add_MainWindow", "English"))
        self.new_entry_language_combobox.setItemText(0, _translate("Add_MainWindow", "English"))
        self.new_entry_language_combobox.setItemText(1, _translate("Add_MainWindow", "Spanish"))
        self.new_entry_language_combobox.setItemText(2, _translate("Add_MainWindow", "French"))
        self.new_entry_language_combobox.setItemText(3, _translate("Add_MainWindow", "Italian"))
        self.new_entry_language_combobox.setItemText(4, _translate("Add_MainWindow", "German"))
        self.new_entry_language_combobox.setItemText(5, _translate("Add_MainWindow", "Portuguese"))
        self.label_10.setText(_translate("Add_MainWindow", "Language"))
        self.label_9.setText(_translate("Add_MainWindow", "Entry"))
        self.get_translations_button.setText(_translate("Add_MainWindow", "Translate"))
        self.label_11.setText(_translate("Add_MainWindow", "Portuguese"))
        self.clear_button.setText(_translate("Add_MainWindow", "Clear"))

    def clear_entry(self):
        self.english_textEdit.setText('')
        self.spanish_textEdit.setText('')
        self.french_textEdit.setText('')
        self.italian_textEdit.setText('')
        self.german_textEdit.setText('')
        self.portuguese_textEdit.setText('')
        self.new_entry_textEdit.setText('')

    def get_translations(self):
        try:
            translator = Translator()
            # translator = google_translator()
            self.base_list = ['en', 'es', 'fr', 'it', 'de', 'pt']

            if self.new_entry_language_combobox.currentText() == 'English':
                self.base_language = self.base_list[0]
            elif self.new_entry_language_combobox.currentText() == 'Spanish':
                self.base_language = self.base_list[1]
            elif self.new_entry_language_combobox.currentText() == 'French':
                self.base_language = self.base_list[2]
            elif self.new_entry_language_combobox.currentText() == 'Italian':
                self.base_language = self.base_list[3]
            elif self.new_entry_language_combobox.currentText() == 'German':
                self.base_language = self.base_list[4]
            else:
                self.base_language = self.base_list[5]

            translate_text = translator.translate(self.new_entry_textEdit.toPlainText(), src=self.base_language, dest='en')
            self.english_textEdit.setText(translate_text.text)
            translate_text = translator.translate(self.new_entry_textEdit.toPlainText(), src=self.base_language, dest='es')
            self.spanish_textEdit.setText(translate_text.text)
            translate_text = translator.translate(self.new_entry_textEdit.toPlainText(), src=self.base_language, dest='fr')
            self.french_textEdit.setText(translate_text.text)
            translate_text = translator.translate(self.new_entry_textEdit.toPlainText(), src=self.base_language, dest='it')
            self.italian_textEdit.setText(translate_text.text)
            translate_text = translator.translate(self.new_entry_textEdit.toPlainText(), src=self.base_language, dest='de')
            self.german_textEdit.setText(translate_text.text)
            translate_text = translator.translate(self.new_entry_textEdit.toPlainText(), src=self.base_language, dest='pt')
            self.portuguese_textEdit.setText(translate_text.text)
        except Exception as e:
            print(getattr(e, 'message', repr(e)))
            self.validation_instance.download_error()

    def get_pronunciation(self, button_value):
        if button_value == 1:
            self.phrase = self.english_textEdit.toPlainText()
            self.language = 'en'
        if button_value == 2:
            self.phrase = self.spanish_textEdit.toPlainText()
            self.language = 'es'
        if button_value == 3:
            self.phrase = self.french_textEdit.toPlainText()
            self.language = 'fr'
        if button_value == 4:
            self.phrase = self.italian_textEdit.toPlainText()
            self.language = 'it'
        if button_value == 5:
            self.phrase = self.german_textEdit.toPlainText()
            self.language = 'de'
        if button_value == 6:
            self.phrase = self.portuguese_textEdit.toPlainText()
            self.language = 'pt'
        if self.phrase == '':
            pass
        else:
            self.sound_instance.play_pronunciation(self.phrase, self.language)

    def no_blanks(self):
        self.validation_instance.blank_entry_validation()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Add_MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Add_MainWindow()
    ui.setupUi(Add_MainWindow)
    Add_MainWindow.show()
    sys.exit(app.exec_())
