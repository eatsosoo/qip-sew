import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel


# Tạo lớp cửa sổ phụ
class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cửa sổ phụ")
        self.setGeometry(400, 300, 300, 200)

        # Giao diện đơn giản cho cửa sổ phụ
        layout = QVBoxLayout()
        label = QLabel("Đây là cửa sổ phụ")
        layout.addWidget(label)
        self.setLayout(layout)


# Tạo lớp cửa sổ chính
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cửa sổ chính")
        self.setGeometry(300, 200, 400, 300)

        # Tạo nút bấm để mở cửa sổ phụ
        button = QPushButton("Mở cửa sổ phụ", self)
        button.setGeometry(100, 100, 200, 50)
        button.clicked.connect(self.open_second_window)

        # Đối tượng cửa sổ phụ
        self.second_window = None

    def open_second_window(self):
        # Khởi tạo cửa sổ phụ và hiển thị
        if not self.second_window:  # Nếu cửa sổ chưa tồn tại
            self.second_window = SecondWindow()
        self.second_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec())
