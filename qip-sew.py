# -*- coding: utf-8 -*-
import sys
import yaml
import logging
from functools import partial
from PySide import QtCore, QtGui
from PySide.QtGui import QFontDatabase
from datetime import datetime
from constants import HORIZONTAL_HEADERS, VERTICAL_HEADERS, COLUMNS, SEW_ERRORS, PRIMARY_COLOR, DANGER_COLOR, STYLE_SCROLLBAR

# Configure logging
logging.basicConfig(filename='sew_errors.log', level=logging.INFO, format='%(asctime)s - %(message)s')

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)
STATION = config["STATION"]

class SecondWindow(QtGui.QWidget):
    error_count_updated = QtCore.Signal(str, int)

    def __init__(self, parent=None):
        super(SecondWindow, self).__init__(parent)
        self.resize(1024, 768)
        self.setWindowTitle(u"Other Sewing Errors {}".format(STATION))
        self.layout = QtGui.QVBoxLayout(self)

        sew_error_layout = QtGui.QGridLayout()
        self.layout.addLayout(sew_error_layout)

        row = 0
        col = 0

        self.error_counts = {key: 0 for key in SEW_ERRORS.keys()}

        for key, value in SEW_ERRORS.items():
            block_layout = QtGui.QVBoxLayout()

            label = QtGui.QLabel(value)
            label.setAlignment(QtCore.Qt.AlignCenter)
            font = label.font()
            font.setPointSize(12)  # Increase the font size
            label.setFont(font)
            label.setFixedHeight(40)  # Set fixed height for the label

            h_layout = QtGui.QHBoxLayout()
            decrement_button = QtGui.QPushButton("-")
            decrement_button.setStyleSheet("background-color: red; color: white; font-size: 20px;")
            decrement_button.setFixedSize(40, 40)  # Set fixed size for decrement button
            increment_button = QtGui.QPushButton("+")
            increment_button.setStyleSheet("background-color: {}; color: white; font-size: 20px;".format(PRIMARY_COLOR))
            increment_button.setFixedSize(40, 40)  # Set fixed size for increment button

            count_label = QtGui.QLabel("0")
            count_label.setStyleSheet("background-color: white; color: black; font-size: 20px;")
            count_label.setAlignment(QtCore.Qt.AlignCenter)
            count_label.setObjectName("count_label")

            decrement_button.clicked.connect(partial(self.update_error_count, key, -1))
            increment_button.clicked.connect(partial(self.update_error_count, key, 1))

            h_layout.addWidget(decrement_button)
            h_layout.addWidget(count_label)
            h_layout.addWidget(increment_button)

            block_widget = QtGui.QWidget()
            block_layout = QtGui.QVBoxLayout(block_widget)
            block_layout.addWidget(label)
            block_layout.addLayout(h_layout)

            # Apply border and border radius to the block
            block_widget.setStyleSheet("""
                QWidget {
                    border: 1px solid black;
                    border-radius: 6px;
                    padding: 5px;
                    background-color: white;
                }
            """)

            sew_error_layout.addWidget(block_widget, row, col)
            col += 1

            if col == 4:
                col = 0
                row += 1

        # Set equal column stretch factors
        for i in range(4):
            sew_error_layout.setColumnStretch(i, 1)

    def update_error_count(self, key, delta):
        self.error_counts[key] += delta
        self.error_counts[key] = max(0, self.error_counts[key])  # Ensure count doesn't go below 0
        self.update_error_labels(key)

        # Emit the signal to notify the main window
        self.error_count_updated.emit(key, delta)

    def update_error_labels(self, key):
        for widget in self.findChildren(QtGui.QWidget):
            if isinstance(widget, QtGui.QLabel) and widget.text() in SEW_ERRORS[key]:
                count_label = widget.parent().findChild(QtGui.QLabel, "count_label")
                if count_label:
                    count_label.setText(str(self.error_counts[key]))

class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle(u"QIP Sewing Inspection {}".format(STATION))
        self.resize(1024, 768)
        self.second_window = None
        self.layout = QtGui.QVBoxLayout(self)

        self.grid_layout = QtGui.QGridLayout()
        self.grid_layout.setVerticalSpacing(20)  # Adjust vertical spacing between rows
        self.grid_layout.setHorizontalSpacing(10)  # Adjust horizontal spacing between columns
        self.layout.addLayout(self.grid_layout)

        # Load the custom font
        font_id = QFontDatabase.addApplicationFont("fonts/Roboto-Regular.ttf")
        if font_id == -1:
            print("Failed to load the custom font!")
        else:
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            print("Loaded font: {}".format(font_family))
        
            # Set the custom font globally
            font = QtGui.QFont(font_family, 12)  # Font size 12
            QtGui.QApplication.setFont(font)

        # 1. Add input field section
        label = QtGui.QLabel(u"Chỉ lệnh")
        self.grid_layout.addWidget(label, 1, 0)
        font = label.font()
        font.setPointSize(12)  # Increase the font size
        label.setFont(font)
        input_field = QtGui.QLineEdit()
        input_field.setFixedSize(200, 30)  # Increase input field size

        # Set font size for input field text
        input_font = input_field.font()
        input_font.setPointSize(12)  # Set the desired font size
        input_field.setFont(input_font)

        self.grid_layout.addWidget(input_field, 1, 1)
        self.inputs = [input_field]

        # Add button beside the input field
        button = QtGui.QPushButton(u"Xác nhận")
        button.setStyleSheet("background-color: {}; color: white; font-size: 14px; border-radius: 5px;".format(PRIMARY_COLOR))
        button.setFixedSize(100, 30)  # Increase button size
        self.grid_layout.addWidget(button, 1, 2)

        # Label to display the input value
        self.display_label = QtGui.QLabel("")
        self.display_label.setFont(font)  # Set the same font size for display label
        self.grid_layout.addWidget(self.display_label, 1, 3)

        # Connect button click to the function
        button.clicked.connect(lambda: self.display_input_value(input_field))

        # Store the command value
        self.mo_no = input_field.text()

        # Add button to open the error window
        others_error_window_btn = QtGui.QPushButton(u"Lỗi khác")
        others_error_window_btn.setStyleSheet("background-color: {}; color: white; font-size: 14px; border-radius: 5px;".format(DANGER_COLOR))
        others_error_window_btn.setFixedSize(150, 30)
        self.grid_layout.addWidget(others_error_window_btn, 1, 4)
        others_error_window_btn.clicked.connect(self.open_other_error_window)

        # 2. Add table section
        self.table_widget = QtGui.QTableWidget(3, 11)
        self.table_widget.setHorizontalHeaderLabels(HORIZONTAL_HEADERS)
        self.table_widget.setVerticalHeaderLabels(VERTICAL_HEADERS)
        self.table_widget.verticalHeader().setFixedWidth(120)

        # Set font for table cells
        font = self.table_widget.font()
        font.setPointSize(12)  # Increase the font size to 12
        self.table_widget.setFont(font)

        # Set font for headers
        header_font = self.table_widget.horizontalHeader().font()
        header_font.setPointSize(14)  # Increase font size for headers
        self.table_widget.horizontalHeader().setFont(header_font)
        self.table_widget.verticalHeader().setFont(header_font)

        # Data for the first two rows
        self.inspection_data = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Số hàng cần kiểm
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Số hàng lỗi
        ]

        # Fill data into the table
        for row_idx, row_data in enumerate(self.inspection_data):
            for col_idx, value in enumerate(row_data):
                item = QtGui.QTableWidgetItem(str(value))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # Make cells read-only
                self.table_widget.setItem(row_idx, col_idx, item)

        # Calculate the percentage for the third row
        self.calculate_percentages()

        # Automatically resize column width to fit the window
        header = self.table_widget.horizontalHeader()
        header.setResizeMode(QtGui.QHeaderView.Stretch)

        # Set fixed height for the table to fit approximately three rows
        self.table_widget.setFixedHeight(118)

        # Apply border to all elements in the table
        self.table_widget.setStyleSheet("""
            QHeaderView::section {
                border: 1px solid #f0f0f0;
                border-left: none;
                background-color: white;
                font-size: 14px;
            }
        """)

        self.layout.addWidget(self.table_widget)

        # 3. Add timeline selector and quantity input
        timeline_label = QtGui.QLabel(u"Chọn khung giờ")
        timeline_label.setFont(font)
        self.grid_layout.addWidget(timeline_label, 2, 0)

        self.timeline_combo = QtGui.QComboBox()
        self.timeline_combo.addItems(HORIZONTAL_HEADERS)
        self.timeline_combo.setFont(font)
        self.timeline_combo.setCurrentIndex(self.get_current_timeline())
        self.timeline_combo.setStyleSheet("background-color: white;")  # Set font size for the combo box
        self.grid_layout.addWidget(self.timeline_combo, 2, 1)

        quantity_label = QtGui.QLabel(u"Số lượng cần kiểm")
        quantity_label.setFont(font)
        self.grid_layout.addWidget(quantity_label, 2, 2)

        self.quantity_input = QtGui.QLineEdit()
        self.quantity_input.setFont(font)
        self.grid_layout.addWidget(self.quantity_input, 2, 3)

        update_button = QtGui.QPushButton(u"Cập nhật")
        update_button.setStyleSheet("background-color: {}; color: white; font-size: 14px; border-radius: 5px;".format(PRIMARY_COLOR))
        update_button.setFixedSize(150, 30)
        update_button.clicked.connect(lambda: self.update_quantity())
        self.grid_layout.addWidget(update_button, 2, 4)

        # 4. Add sewing error section
        scroll_area = QtGui.QScrollArea()
        scroll_area.setWidgetResizable(True)  # Cho phép widget thay đổi kích thước theo scroll area
        scroll_area.setStyleSheet(STYLE_SCROLLBAR)  # Thêm thanh cuộn theo style đã thiết lập
        # scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        # scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        
        # Tạo widget để chứa sew_error_layout
        sew_error_widget = QtGui.QWidget()
        sew_error_layout = QtGui.QGridLayout(sew_error_widget)

        scroll_area.setWidget(sew_error_widget)  # Đặt widget chứa layout vào scroll area
        self.layout.addWidget(scroll_area)

        row = 0
        col = 0

        self.error_counts = {key: 0 for key in COLUMNS.keys()}
        index = 0

        for key, value in COLUMNS.items():
            index += 1
            block_layout = QtGui.QVBoxLayout()

            label = QtGui.QLabel(u"{}. {}".format(index, value))
            label.setAlignment(QtCore.Qt.AlignCenter)
            font = label.font()
            font.setPointSize(12)  # Increase the font size
            label.setFont(font)
            label.setFixedHeight(40)  # Set fixed height for the label

            h_layout = QtGui.QHBoxLayout()
            decrement_button = QtGui.QPushButton("-")
            decrement_button.setStyleSheet("background-color: red; color: white; font-size: 20px;")
            decrement_button.setFixedSize(80, 40)  # Set fixed size for decrement button
            increment_button = QtGui.QPushButton("+")
            increment_button.setStyleSheet("background-color: {}; color: white; font-size: 20px;".format(PRIMARY_COLOR))
            increment_button.setFixedSize(80, 40)  # Set fixed size for increment button

            count_label = QtGui.QLabel("0")
            count_label.setStyleSheet("background-color: white; color: black; font-size: 20px;")
            count_label.setAlignment(QtCore.Qt.AlignCenter)
            count_label.setObjectName("count_label")

            decrement_button.clicked.connect(partial(self.update_error_count, key, -1))
            increment_button.clicked.connect(partial(self.update_error_count, key, 1))

            h_layout.addWidget(decrement_button)
            h_layout.addWidget(count_label)
            h_layout.addWidget(increment_button)

            block_widget = QtGui.QWidget()
            block_layout = QtGui.QVBoxLayout(block_widget)
            block_layout.addWidget(label)
            block_layout.addLayout(h_layout)

            # Apply border and border radius to the block
            block_widget.setStyleSheet("""
                QWidget {
                    border: 1px solid black;
                    border-radius: 6px;
                    padding: 5px;
                    background-color: white;
                }
            """)

            sew_error_layout.addWidget(block_widget, row, col)
            col += 1

            if col == 4:
                col = 0
                row += 1

        # Set equal column stretch factors
        for i in range(4):
            sew_error_layout.setColumnStretch(i, 1)

    def get_current_timeline(self):
        current_time = datetime.now().time()
        for idx, header in enumerate(HORIZONTAL_HEADERS):
            start_time_str, end_time_str = header.split('-')
            start_time = datetime.strptime(start_time_str, "%H:%M").time()
            end_time = datetime.strptime(end_time_str, "%H:%M").time()
            if start_time <= current_time <= end_time:
                return idx
        return 0

    def update_error_count(self, key, delta):
        self.error_counts[key] += delta
        self.error_counts[key] = max(0, self.error_counts[key])  # Ensure count doesn't go below 0
        self.update_error_labels(key, delta)
        
        logging.info(u"Update '{}' count changed by {}. New count: {}".format(key, delta, self.error_counts[key]))

        # Update the error quantity and recalculate the error rate
        timeline_idx = self.get_current_timeline()
        if timeline_idx is not None:
            self.inspection_data[1][timeline_idx] += delta
            self.inspection_data[1][timeline_idx] = max(0, self.inspection_data[1][timeline_idx])  # Ensure count doesn't go below 0
            self.update_error_quantity(timeline_idx)
            self.calculate_percentages()
    
    def update_table_from_second_window(self, key, delta):
        print(key, delta)
        timeline_idx = self.get_current_timeline()
        if timeline_idx is not None:
            self.inspection_data[1][timeline_idx] += delta
            self.inspection_data[1][timeline_idx] = max(0, self.inspection_data[1][timeline_idx])  # Ensure count doesn't go below 0
            self.update_error_quantity(timeline_idx)
            self.calculate_percentages()

    def update_error_quantity(self, timeline_idx):
        error_quantity = self.inspection_data[1][timeline_idx]
        item = QtGui.QTableWidgetItem(str(error_quantity))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # Make cells read-only
        self.table_widget.setItem(1, timeline_idx, item)

    def update_error_labels(self, key, delta):
        for widget in self.findChildren(QtGui.QWidget):
            if isinstance(widget, QtGui.QLabel) and widget.text() in COLUMNS[key]:
                count_label = widget.parent().findChild(QtGui.QLabel, "count_label")
                if count_label:
                    count_label.setText(str(self.error_counts[key]))

    def calculate_percentages(self):
        for col_idx in range(len(self.inspection_data[0])):
            total_checked = self.inspection_data[0][col_idx]
            errors = self.inspection_data[1][col_idx]
            if total_checked > 0:
                percentage = (errors / float(total_checked) * 100)  # Convert to float for division
            else:
                percentage = 0  # Avoid division by zero
            percentage_item = QtGui.QTableWidgetItem("{}%".format(round(percentage, 2)))
            percentage_item.setTextAlignment(QtCore.Qt.AlignCenter)
            percentage_item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # Make cells read-only
            self.table_widget.setItem(2, col_idx, percentage_item)

    def display_input_value(self, input_field):
        self.display_label.setText(input_field.text())

    def open_other_error_window(self):
        print("Opening other error window")
        # Khởi tạo cửa sổ phụ và hiển thị
        if not self.second_window:  # Nếu cửa sổ chưa tồn tại
            self.second_window = SecondWindow()
        self.second_window.show()
        self.second_window.error_count_updated.connect(self.update_table_from_second_window)

    def update_quantity(self):
        timeline_idx = self.timeline_combo.currentIndex()
        try:
            quantity = int(self.quantity_input.text())
            self.inspection_data[0][timeline_idx] = quantity
            item = QtGui.QTableWidgetItem(str(quantity))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # Make cells read-only
            self.table_widget.setItem(0, timeline_idx, item)
            self.calculate_percentages()
        except ValueError:
            QtGui.QMessageBox.warning(self, "Invalid Input", "Please enter a valid number for quantity.")

if __name__ == "__main__":
    app = QtGui.QApplication([])
    first_window = MainWindow()
    first_window.show()
    sys.exit(app.exec_())