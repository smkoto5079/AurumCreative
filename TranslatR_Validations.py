from PyQt5.QtWidgets import QMessageBox


class Validations:
    def level_checkbox_validation(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        # setting message for Message Box
        msg.setText("You must select at least 1 Study Level.")

        # setting Message box window title
        msg.setWindowTitle("Missing Information")

        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)

        # start the app
        retval = msg.exec_()

    def material_checkbox_validation(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        # setting message for Message Box
        msg.setText("You must select at least 1 Study Material.")

        # setting Message box window title
        msg.setWindowTitle("Missing Information")

        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)

        # start the app
        retval = msg.exec_()

    def database_selection_validation(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        # setting message for Message Box
        msg.setText("You must select at least 1 entry.")

        # setting Message box window title
        msg.setWindowTitle("Missing Information")

        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)

        # start the app
        retval = msg.exec_()

    def download_error(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        # setting message for Message Box
        msg.setText("An error occurred in translation.  Please try again.")

        # setting Message box window title
        msg.setWindowTitle("Download Error")

        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)

        # start the app
        retval = msg.exec_()

    def blank_entry_validation(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        # setting message for Message Box
        msg.setText("You must have at least 1 entry.")

        # setting Message box window title
        msg.setWindowTitle("Invalid Information")

        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)

        # start the app
        retval = msg.exec_()

    def no_sound(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        # setting message for Message Box
        msg.setText("Could not play sound file.")

        # setting Message box window title
        msg.setWindowTitle("Invalid Information")

        # declaring buttons on Message Box
        msg.setStandardButtons(QMessageBox.Ok)

        # start the app
        retval = msg.exec_()
