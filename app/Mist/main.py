import sys
import random

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView

from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.browser = QWebEngineView()

        layout = self.ui.widget.layout()

        if layout is None:
            from PyQt6.QtWidgets import QVBoxLayout
            layout = QVBoxLayout(self.ui.widget)
            self.ui.widget.setLayout(layout)

        layout.addWidget(self.browser)

        self.ui.listWidget.itemClicked.connect(self.load_game)

        self.ui.listWidget.itemClicked.connect(self.load_game)

        random_item = self.ui.listWidget.item(
            random.randint(0, self.ui.listWidget.count() - 1)
        )

        self.ui.listWidget.setCurrentItem(random_item)
        self.load_game(random_item)

    def load_game(self, item):
        game = item.text()

        games = {
            "Aimlabs": "https://store.steampowered.com/app/714010/Aimlabs/",
            "Balatro": "https://store.steampowered.com/app/2379780/Balatro/",
            "Baldi's Basics Classic Remastered": "https://store.steampowered.com/app/1712830/Baldis_Basics_Classic_Remastered/",
            "Buckshot Roulette": "https://store.steampowered.com/app/2835570/Buckshot_Roulette/",
            "Counter-Strike 2": "https://store.steampowered.com/app/730/CounterStrike_2/",
            "Cry of Fear": "https://store.steampowered.com/app/223710/Cry_of_Fear/",
            "A Dance of Fire and Ice": "https://store.steampowered.com/app/977950/A_Dance_of_Fire_and_Ice/",
            "Doki Doki Literature Club": "https://store.steampowered.com/app/698780/Doki_Doki_Literature_Club/",
            "The Exit 8": "https://store.steampowered.com/app/2653790/The_Exit_8/",
            "Firewatch": "https://store.steampowered.com/app/383870/Firewatch/",
            "Geometry Dash": "https://store.steampowered.com/app/322170/Geometry_Dash/",
            "Hatred": "https://store.steampowered.com/app/341940/Hatred/",
            "Mortal Kombat 11": "https://store.steampowered.com/app/976310/Mortal_Kombat_11/",
            "NEEDY STREAMER OVERLOAD": "https://store.steampowered.com/app/1451940/NEEDY_STREAMER_OVERLOAD/",
            "POSTAL": "https://store.steampowered.com/app/232770/POSTAL/",
            "POSTAL 2": "https://store.steampowered.com/app/223470/POSTAL_2/",
            "Quaver": "https://store.steampowered.com/app/980610/Quaver/",
            "skate.": "https://store.steampowered.com/app/3354750/skate/",
            "Terraria": "https://store.steampowered.com/app/105600/Terraria/",
            "Titanfall 2": "https://store.steampowered.com/app/1237970/Titanfall_2/",
            "Tom Clancy's Rainbow Six Siege": "https://store.steampowered.com/app/359550/Tom_Clancys_Rainbow_Six_Siege/",
            "Touhou Hero of Ice Fairy": "https://store.steampowered.com/app/1955830/Touhou_Hero_of_Ice_Fairy/",
            "ULTRAKILL": "https://store.steampowered.com/app/1229490/ULTRAKILL/",
            "Undertale": "https://store.steampowered.com/app/391540/Undertale/",
        }

        if game in games:
            self.browser.setUrl(QUrl(games[game]))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())