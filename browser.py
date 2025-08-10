import sys
import os
import time
import requests
import subprocess
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLineEdit, QWidget, QHBoxLayout, QTabWidget, QTextEdit, QFileDialog
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl, QThread, pyqtSignal
from PyQt6.QtGui import QPalette, QColor

class FileDownloader(QThread):
    progress = pyqtSignal(str)

    def __init__(self, download_link, download_dir):
        super().__init__()
        self.download_link = download_link
        self.download_dir = os.path.abspath(download_dir)

    def run(self):
        os.makedirs(self.download_dir, exist_ok=True)
        response = requests.get(self.download_link, stream=True)
        total_size = int(response.headers.get('content-length', 0))
        file_name = self.download_link.split("/")[-1]
        file_path = os.path.join(self.download_dir, file_name)
        with open(file_path, "wb") as file:
            downloaded_size = 0
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
                    downloaded_size += len(chunk)
                    self.progress.emit(f"Downloading: {downloaded_size / total_size * 100:.2f}%")
        self.progress.emit("Download Complete")

class SimpleBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Browser")
        self.setGeometry(100, 100, 1200, 800)

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.setCentralWidget(self.tabs)

        self.create_new_tab("https://www.example.com", is_web=True)

    def create_new_tab(self, content, is_web=True):
        new_tab = QWidget()
        layout = QVBoxLayout()

        browser = QWebEngineView() if is_web else QTextEdit()
        if is_web:
            browser.setUrl(QUrl(content))
        else:
            browser.setPlainText(content)
            browser.setReadOnly(False)

        url_bar = QLineEdit()
        url_bar.setPlaceholderText("Enter URL, search query, or file link...")
        url_bar.textChanged.connect(lambda: self.check_magnet_link(url_bar, download_button))
        url_bar.returnPressed.connect(lambda: self.load_content(url_bar, browser))

        back_button = QPushButton("◀")
        back_button.clicked.connect(lambda: browser.back() if isinstance(browser, QWebEngineView) else None)

        forward_button = QPushButton("▶")
        forward_button.clicked.connect(lambda: browser.forward() if isinstance(browser, QWebEngineView) else None)

        refresh_button = QPushButton("⟳")
        refresh_button.clicked.connect(lambda: browser.reload() if isinstance(browser, QWebEngineView) else None)

        new_tab_button = QPushButton("＋")
        new_tab_button.clicked.connect(lambda: self.create_new_tab("https://www.example.com", is_web=True))

        download_button = QPushButton("⬇")
        download_button.setEnabled(False)
        download_button.clicked.connect(lambda: self.select_download_directory(url_bar.text().strip()))

        nav_layout = QHBoxLayout()
        nav_layout.addWidget(back_button)
        nav_layout.addWidget(forward_button)
        nav_layout.addWidget(refresh_button)
        nav_layout.addWidget(url_bar)
        nav_layout.addWidget(new_tab_button)
        nav_layout.addWidget(download_button)

        layout.addLayout(nav_layout)
        layout.addWidget(browser)
        new_tab.setLayout(layout)
        self.tabs.addTab(new_tab, "New Tab" if isinstance(browser, QTextEdit) else "Web Tab")
        self.tabs.setCurrentWidget(new_tab)

        if isinstance(browser, QWebEngineView):
            url_bar.setText(browser.url().toString())
            browser.urlChanged.connect(lambda url: url_bar.setText(url.toString()))

    def check_magnet_link(self, url_bar, download_button):
        if url_bar.text().startswith("magnet:?xt="):
            download_button.setEnabled(True)
            download_button.setStyleSheet("background-color: green; color: white;")
        else:
            download_button.setEnabled(False)
            download_button.setStyleSheet("")

    def load_content(self, url_bar, browser):
        content = url_bar.text().strip()
        if content.startswith("magnet:?xt="):
            subprocess.Popen(["qbittorrent", content])
        elif content.startswith("http") and (".torrent" in content or ".zip" in content or ".exe" in content):
            self.select_download_directory(content)
        elif isinstance(browser, QWebEngineView):
            if "." in content or content.startswith("http"):
                browser.setUrl(QUrl(content))
            else:
                search_url = f"https://www.google.com/search?q={content.replace(' ', '+')}"
                browser.setUrl(QUrl(search_url))
        elif isinstance(browser, QTextEdit):
            browser.setPlainText(content)

    def select_download_directory(self, file_link):
        if file_link.startswith("http"):
            directory = QFileDialog.getExistingDirectory(self, "Select Download Directory")
            if directory:
                directory = os.path.abspath(directory)
                os.makedirs(directory, exist_ok=True)
                self.download_file(file_link, directory)

    def download_file(self, file_link, download_dir):
        self.download_thread = FileDownloader(file_link, download_dir)
        self.download_thread.progress.connect(lambda msg: self.statusBar().showMessage(msg))
        self.download_thread.start()

    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleBrowser()
    window.show()
    sys.exit(app.exec())
