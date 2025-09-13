import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon, QPixmap, QAction
from PyQt6.QtWidgets import QLabel, QMenu, QMenuBar, QWidget, QStatusBar
from PyQt6.QtCore import QSize, Qt, QRect, QMetaObject, QCoreApplication

from new_delhi_weather.new_delhi_weather_app import NewDelhiWeather
from new_delhi_weather.new_delhi_weather_model import NewDelhiWeather as Model
from new_delhi_weather.new_delhi_weather_controller import NewDelhiWeather as Controller
from new_delhi_weather.new_delhi_weather_view import NewDelhiWeather as View


class SystemWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()

        self.new_delhi_weather = None

        self.setObjectName("SystemWindow")
        self.setWindowTitle("Maneki Neko")
        self.setWindowIcon(QIcon(""))
        self.showMaximized()

        #BG logo
        logo_pixmap = QPixmap("Resources/Images/taxseguro.png")
        logo_pixmap.scaled(QSize(200, 200))
        logo_label = QLabel()
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(logo_label)

        # Main Menu setup
        self.menubar = QMenuBar(self)
        self.menubar.setObjectName("menubar")
        self.menu_item_project = QMenu(self.menubar)
        self.menu_item_project.setObjectName("menu_item_project")
        self.menu_item_project.setTitle("Project")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuEdit.setTitle("Edit")
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.action_weather_new_delhi = QAction(self)
        self.action_weather_new_delhi.setObjectName("action_weather_new_delhi")
        self.action_weather_new_delhi.setText("Climate New delhi")
        self.action_weather_new_delhi.triggered.connect(self.setupNewDelhiWeatherModule)
        self.actionOpen = QAction(self)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.setText("Open")
        self.actionSave = QAction(self)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.setText("Save")
        self.actionExit = QAction(self)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setText("Exit")
        self.action1 = QAction(self)
        self.action1.setObjectName("action1")
        self.action1.setText("1")
        self.action2 = QAction(self)
        self.action2.setObjectName("action2")
        self.action2.setText("2")

        self.menubar.addAction(self.menu_item_project.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menu_item_project.addAction(self.action_weather_new_delhi)
        self.menu_item_project.addAction(self.actionOpen)
        self.menu_item_project.addAction(self.actionSave)
        self.menu_item_project.addSeparator()
        self.menu_item_project.addAction(self.actionExit)
        self.menuEdit.addAction(self.action1)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.action2)

        QMetaObject.connectSlotsByName(self)

        self._model = Model("Initial Value")
        self.new_delhi_weather = View()
        self._controller = Controller(self._model, self.new_delhi_weather)

    def setupNewDelhiWeatherModule(self):
        if self.new_delhi_weather is None:
            self.new_delhi_weather = View()
        self.setCentralWidget(self.new_delhi_weather)

        self.new_delhi_weather.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    systemWindow = SystemWindow()
    systemWindow.show()

    sys.exit(app.exec())
