import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Navigation_bar_options
        navigation_bar = QToolBar()
        self.addToolBar(navigation_bar)

        back_button = QAction('Back', self)
        back_button.triggered.connect(self.browser.back)
        navigation_bar.addAction(back_button)

        forward_button = QAction('Forward', self)
        forward_button.triggered.connect(self.browser.forward)
        navigation_bar.addAction(forward_button)

        refresh_button = QAction('Refresh', self)
        refresh_button.triggered.connect(self.browser.reload)
        navigation_bar.addAction(refresh_button)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.fetch_url)
        navigation_bar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    def fetch_url(self):
        url1 = self.url_bar.text()
        if '.com' in url1:
            url = 'http://'+url1
            self.browser.setUrl(QUrl(url))
        else:
            url = 'https://www.google.com/search?q='+url1
            self.browser.setUrl(QUrl(url))


app = QApplication(sys.argv)
QApplication.setApplicationName('Python Web Browser')
window = MainWindow()
app.exec_()
