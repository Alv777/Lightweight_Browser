import sys
from PyQt5 import (QtCore, QtWidgets)
from PyQt5.QtWidgets import (QMainWindow, QPushButton, QLabel, QLineEdit)
from PyQt5.QtWidgets import (QFormLayout, QSizePolicy, QAction, QToolBar, QApplication)
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class TabWidget(QtWidgets.QTabWidget):
    def __init__(self, *args, **kwargs):
        super(TabWidget, self).__init__(*args, **kwargs)
        self.pinned_tabs = []
        
    def contextMenuEvent(self, event):
        index = self.tabBar().tabAt(event.pos())
        if index >= 0:
            menu = QtWidgets.QMenu(self)
            close_action = menu.addAction("Close Tab")
            close_action.triggered.connect(lambda: self.tabCloseRequested.emit(index))
            widget = self.widget(index)
            if widget in self.pinned_tabs:
                close_action.setEnabled(False)
                pin_action = menu.addAction("Unpin")
                pin_action.triggered.connect(lambda: self.unpin_tab(widget))
            else:
                pin_action = menu.addAction("Pin")
                pin_action.triggered.connect(lambda: self.pin_tab(widget))
            menu.exec_(event.globalPos())
            
    def pin_tab(self, widget):
        if widget not in self.pinned_tabs:
            self.pinned_tabs.append(widget)
            self.tabBar().setTabButton(self.indexOf(widget), QtWidgets.QTabBar.RightSide, None)
            
    def unpin_tab(self, widget):
        if widget in self.pinned_tabs:
            self.pinned_tabs.remove(widget)
            index = self.indexOf(widget)
            close_button = QtWidgets.QToolButton(self.tabBar())
            close_button.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_TitleBarCloseButton))
            close_button.clicked.connect(lambda: self.tabCloseRequested.emit(index))
            self.tabBar().setTabButton(index, QtWidgets.QTabBar.RightSide, close_button)

class SettingsWindow(QMainWindow):
    def __init__(self):
        super(SettingsWindow, self).__init__()
        

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

        settings_tab = QAction('Settings', self)
        settings_tab.triggered.connect(self.settingsTabHandler)
        navbar.addAction(settings_tab)
        self.settings_tab_open = False
        self.browser.urlChanged.connect(self.update_url)
        
        self.resize(800, 600) # Set width and height (Doesn't even work but at least it's a reasonable size lol)
        
    def newTabHandler(self):
        tab_widget = self.parentWidget().parentWidget()
        print(tab_widget)
        win = MainWindow()
        tab_widget.addTab(win, "New Tab")
    
    def settingsTabHandler(self):
        tab_widget = self.parentWidget().parentWidget()
        settings_tab_open = False
        for i in range(tab_widget.count()):
            if tab_widget.tabText(i) == "Settings":
                settings_tab_open = True
                break
        if not settings_tab_open:
            win = SettingsWindow()
            tab_widget.addTab(win, "Settings")
        else:
            # Mostrar un mensaje al usuario o simplemente no hacer nada
            pass
    
    def close_tab(self, index):
        tab_widget = self.parentWidget() 
        tab_widget = tab_widget.parentWidget()
        tab_widget.removeTab(index)
        if tab_widget.count() == 0:
            self.newTabHandler()

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
    tabs = TabWidget()
    win = MainWindow()
    tabs.addTab(win, "New Tab")
    tabs.show()
    tabs.setTabsClosable(True)
    tabs.tabCloseRequested.connect(win.close_tab)
    tabs.setDocumentMode(True)
    tabs.setMovable(True)
    sys.exit (app.exec_())