import sys
from PyQt5 import QtWidgets, uic

# Paths to your UI files
ui_file_main = "UI/Front_page.ui"
ui_file_1 = "UI/Line_Rejection.ui"
ui_file_2 = "UI/Secondary_Level.ui"
ui_file_3 = "UI/POKA-YOKE.ui"
ui_file_4 = "UI/line_setup.ui"
ui_file_5 = "UI/sta_1.ToolMonitoring.ui"

class MyApp(QtWidgets.QDialog):  # Inherit from QDialog
    def __init__(self):
        super(MyApp, self).__init__()
        uic.loadUi(ui_file_main, self)  # Load the main .ui file
        self.show()

        # Connect buttons to functions
        self.Line_rejection_BTN.clicked.connect(self.open_ui1)
        self.Maintainance_BTN.clicked.connect(self.open_ui2)
        self.POKAYOKE_BTN.clicked.connect(self.open_ui3)
        self.Line_Setup_BTN.clicked.connect(self.open_ui4)
        self.Tool_Monitoring_BTN.clicked.connect(self.open_ui5)

    def open_ui1(self):
        self.ui1_window = QtWidgets.QDialog()  # Create a new dialog window
        uic.loadUi(ui_file_1, self.ui1_window)  # Load the UI for the first button
        self.ui1_window.show()  # Show the UI

    def open_ui2(self):
        self.ui2_window = QtWidgets.QDialog()  # Create a new dialog window
        uic.loadUi(ui_file_2, self.ui2_window)  # Load the UI for the second button
        self.ui2_window.show()  # Show the UI

    def open_ui3(self):
        self.ui3_window = QtWidgets.QDialog()  # Create a new dialog window
        uic.loadUi(ui_file_3, self.ui3_window)  # Load the UI for the third button
        self.ui3_window.show()  # Show the UI

    def open_ui4(self):
        self.ui4_window = QtWidgets.QDialog()  # Create a new dialog window
        uic.loadUi(ui_file_4, self.ui4_window)  # Load the UI for the fourth button
        self.ui4_window.show()  # Show the UI

    def open_ui5(self):
        self.ui5_window = QtWidgets.QDialog()  # Create a new dialog window
        uic.loadUi(ui_file_5, self.ui5_window)  # Load the UI for the fifth button
        self.ui5_window.show()  # Show the UI

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    sys.exit(app.exec_())
