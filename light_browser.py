import sys
from PyQt5 import (QtCore, QtWidgets)
from PyQt5.QtWidgets import (QMainWindow, QPushButton, QLabel, QLineEdit)
from PyQt5.QtWidgets import (QFormLayout, QSizePolicy, QAction, QToolBar, QApplication)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        

        # Navigation Bar
        navbar = QToolBar()
        navbar.setMovable(False)  # Lock the toolbar
        self.addToolBar(navbar)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
        
        new_tab = QAction('New Tab', self)
        new_tab.triggered.connect(self.newTabHandler)
        navbar.addAction(new_tab)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)
        
        self.resize(800, 600) # Set width and height (Doesn't even work but at least it's a reasonable size lol)
        
    def newTabHandler(self):
        tab_widget = self.parentWidget().parentWidget()
        print(tab_widget)
        count = tab_widget.count()
        win = MainWindow()
        tab_widget.addTab(win, "New Tab {}".format(count + 1))
    
    def close_tab(self, index):
        tab_widget = self.parentWidget() 
        tab_widget = tab_widget.parentWidget()
        tab_widget.removeTab(index)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


if (__name__ == "__main__"):
    app = QtWidgets.QApplication(sys.argv)
    QApplication.setStyle("fusion")
    tabs = QtWidgets.QTabWidget()
    win = MainWindow()
    tabs.addTab(win, "New Tab 1" )
    tabs.show()
    tabs.setTabsClosable(True)
    tabs.tabCloseRequested.connect(win.close_tab)
    tabs.setDocumentMode(True)
    tabs.setMovable(True)
    sys.exit (app.exec_())