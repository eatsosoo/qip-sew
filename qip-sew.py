import sys
import yaml
import logging
from PySide6 import QtCore, QtWidgets
from datetime import datetime
from constants import HORIZONTAL_HEADERS, VERTICAL_HEADERS, COLUMNS, SEW_ERRORS, PRIMARY_COLOR, DANGER_COLOR, STYLE_SCROLLBAR

# Configure logging
logging.basicConfig(filename='sew_errors.log', level=logging.INFO, format='%(asctime)s - %(message)s')

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)
STATION = config["STATION"]

class SecondWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(1024, 768)
        self.setWindowTitle(f"Other Sewing Errors {STATION}")
        self.layout = QtWidgets.QVBoxLayout(self)

        sew_error_layout = QtWidgets.QGridLayout()
        self.layout.addLayout(sew_error_layout)

        row = 0
        col = 0

        self.error_counts = {key: 0 for key in SEW_ERRORS.keys()}

        for key, value in SEW_ERRORS.items():
            block_layout = QtWidgets.QVBoxLayout()

            label = QtWidgets.QLabel(value)
            label.setAlignment(QtCore.Qt.AlignCenter)
            font = label.font()
            font.setPointSize(12)  # Increase the font size
            label.setFont(font)
            label.setFixedHeight(40)  # Set fixed height for the label

            h_layout = QtWidgets.QHBoxLayout()
            decrement_button = QtWidgets.QPushButton("-")
            decrement_button.setStyleSheet("background-color: red; color: white; font-size: 20px;")
            decrement_button.setFixedSize(40, 40)  # Set fixed size for decrement button
            increment_button = QtWidgets.QPushButton("+")
            increment_button.setStyleSheet(f"background-color: {PRIMARY_COLOR}; color: white; font-size: 20px;")
            increment_button.setFixedSize(40, 40)  # Set fixed size for increment button

            count_label = QtWidgets.QLabel("0")
            count_label.setStyleSheet("background-color: white; color: black; font-size: 20px;")
            count_label.setAlignment(QtCore.Qt.AlignCenter)
            count_label.setObjectName("count_label")

            decrement_button.clicked.connect(lambda _, k=key: self.update_error_count(k, -1))
            increment_button.clicked.connect(lambda _, k=key: self.update_error_count(k, 1))

            h_layout.addWidget(decrement_button)
            h_layout.addWidget(count_label)
            h_layout.addWidget(increment_button)

            block_widget = QtWidgets.QWidget()
            block_layout = QtWidgets.QVBoxLayout(block_widget)
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
        self.update_error_labels()

    def update_error_labels(self):
        for key, count in self.error_counts.items():
            for widget in self.findChildren(QtWidgets.QWidget):
                if isinstance(widget, QtWidgets.QLabel) and widget.text() == COLUMNS[key]:
                    count_label = widget.parent().findChild(QtWidgets.QLabel, "count_label")
                    if count_label:
                        count_label.setText(str(count))

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(f"QIP Sewing Inspection {STATION}")
        self.resize(1024, 768)
        self.second_window = None
        self.layout = QtWidgets.QVBoxLayout(self)

        self.grid_layout = QtWidgets.QGridLayout()
        self.grid_layout.setVerticalSpacing(20)  # Adjust vertical spacing between rows
        self.grid_layout.setHorizontalSpacing(10)  # Adjust horizontal spacing between columns
        self.layout.addLayout(self.grid_layout)

        # 1. Add input field section
        label = QtWidgets.QLabel("Chỉ lệnh")
        self.grid_layout.addWidget(label, 1, 0)
        font = label.font()
        font.setPointSize(12)  # Increase the font size
        label.setFont(font)
        input_field = QtWidgets.QLineEdit()
        input_field.setFixedSize(200, 30)  # Increase input field size

        # Set font size for input field text
        input_font = input_field.font()
        input_font.setPointSize(12)  # Set the desired font size
        input_field.setFont(input_font)

        self.grid_layout.addWidget(input_field, 1, 1)
        self.inputs = [input_field]

        # Add button beside the input field
        button = QtWidgets.QPushButton("Xác nhận")
        button.setStyleSheet(f"background-color: {PRIMARY_COLOR}; color: white; font-size: 14px; border-radius: 5px;")
        button.setFixedSize(100, 30)  # Increase button size
        self.grid_layout.addWidget(button, 1, 2)

        # Label to display the input value
        self.display_label = QtWidgets.QLabel("")
        self.display_label.setFont(font)  # Set the same font size for display label
        self.grid_layout.addWidget(self.display_label, 1, 3)

        # Connect button click to the function
        button.clicked.connect(lambda: self.display_input_value(input_field))

        # Store the command value
        self.mo_no = input_field.text()

        # Add button to open the error window
        others_error_window_btn = QtWidgets.QPushButton("Lỗi khác")
        others_error_window_btn.setStyleSheet(f"background-color: {DANGER_COLOR}; color: white; font-size: 14px; border-radius: 5px;")
        others_error_window_btn.setFixedSize(150, 30)
        self.grid_layout.addWidget(others_error_window_btn, 1, 4)
        others_error_window_btn.clicked.connect(self.open_other_error_window)

        # 2. Add table section
        self.table_widget = QtWidgets.QTableWidget(3, 11)
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
                item = QtWidgets.QTableWidgetItem(str(value))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # Make cells read-only
                self.table_widget.setItem(row_idx, col_idx, item)

        # Calculate the percentage for the third row
        self.calculate_percentages()

        # Automatically resize column width to fit the window
        header = self.table_widget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        # Set fixed height for the table to fit approximately three rows
        self.table_widget.setFixedHeight(140)

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
        timeline_label = QtWidgets.QLabel("Chọn khung giờ")
        timeline_label.setFont(font)
        self.grid_layout.addWidget(timeline_label, 2, 0)

        self.timeline_combo = QtWidgets.QComboBox()
        self.timeline_combo.addItems(HORIZONTAL_HEADERS)
        self.timeline_combo.setFont(font)
        self.timeline_combo.setCurrentIndex(self.get_current_timeline())
        self.timeline_combo.setStyleSheet("background-color: white;")  # Set font size for the combo box
        self.grid_layout.addWidget(self.timeline_combo, 2, 1)

        quantity_label = QtWidgets.QLabel("Số lượng cần kiểm")
        quantity_label.setFont(font)
        self.grid_layout.addWidget(quantity_label, 2, 2)

        self.quantity_input = QtWidgets.QLineEdit()
        self.quantity_input.setFont(font)
        self.grid_layout.addWidget(self.quantity_input, 2, 3)

        update_button = QtWidgets.QPushButton("Cập nhật")
        update_button.setStyleSheet(f"background-color: {PRIMARY_COLOR}; color: white; font-size: 14px; border-radius: 5px;")
        update_button.setFixedSize(150, 30)
        self.grid_layout.addWidget(update_button, 2, 4)
        update_button.clicked.connect(self.update_quantity)

        # 4. Add sewing error section
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidgetResizable(True)  # Cho phép widget thay đổi kích thước theo scroll area
        scroll_area.setStyleSheet(STYLE_SCROLLBAR)  # Thêm thanh cuộn theo style đã thiết lập
        scroll_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        
        # Tạo widget để chứa sew_error_layout
        sew_error_widget = QtWidgets.QWidget()
        sew_error_layout = QtWidgets.QGridLayout(sew_error_widget)

        scroll_area.setWidget(sew_error_widget)  # Đặt widget chứa layout vào scroll area
        self.layout.addWidget(scroll_area)

        row = 0
        col = 0

        self.error_counts = {key: 0 for key in COLUMNS.keys()}
        index = 0

        for key, value in COLUMNS.items():
            index += 1
            block_layout = QtWidgets.QVBoxLayout()

            label = QtWidgets.QLabel(f"{index}. {value}")
            label.setAlignment(QtCore.Qt.AlignCenter)
            font = label.font()
            font.setPointSize(12)  # Increase the font size
            label.setFont(font)
            label.setFixedHeight(40)  # Set fixed height for the label

            h_layout = QtWidgets.QHBoxLayout()
            decrement_button = QtWidgets.QPushButton("-")
            decrement_button.setStyleSheet("background-color: red; color: white; font-size: 20px;")
            decrement_button.setFixedSize(40, 40)  # Set fixed size for decrement button
            increment_button = QtWidgets.QPushButton("+")
            increment_button.setStyleSheet(f"background-color: {PRIMARY_COLOR}; color: white; font-size: 20px;")
            increment_button.setFixedSize(40, 40)  # Set fixed size for increment button

            count_label = QtWidgets.QLabel("0")
            count_label.setStyleSheet("background-color: white; color: black; font-size: 20px;")
            count_label.setAlignment(QtCore.Qt.AlignCenter)
            count_label.setObjectName("count_label")

            decrement_button.clicked.connect(lambda _, k=key: self.update_error_count(k, -1))
            increment_button.clicked.connect(lambda _, k=key: self.update_error_count(k, 1))

            h_layout.addWidget(decrement_button)
            h_layout.addWidget(count_label)
            h_layout.addWidget(increment_button)

            block_widget = QtWidgets.QWidget()
            block_layout = QtWidgets.QVBoxLayout(block_widget)
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
        return None

    def update_error_count(self, key, delta):
        self.error_counts[key] += delta
        self.error_counts[key] = max(0, self.error_counts[key])  # Ensure count doesn't go below 0
        self.update_error_labels()
        
        logging.info(f"Update '{key}' count changed by {delta}. New count: {self.error_counts[key]}")

        # Update the error quantity and recalculate the error rate
        timeline_idx = self.get_current_timeline()
        if timeline_idx is not None:
            self.inspection_data[1][timeline_idx] += delta
            self.inspection_data[1][timeline_idx] = max(0, self.inspection_data[1][timeline_idx])  # Ensure count doesn't go below 0
            self.update_error_quantity(timeline_idx)
            self.calculate_percentages()

    def update_error_quantity(self, timeline_idx):
        error_quantity = self.inspection_data[1][timeline_idx]
        item = QtWidgets.QTableWidgetItem(str(error_quantity))
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # Make cells read-only
        self.table_widget.setItem(1, timeline_idx, item)

    def update_error_labels(self):
        for key, count in self.error_counts.items():
            for widget in self.findChildren(QtWidgets.QWidget):
                if isinstance(widget, QtWidgets.QLabel) and widget.text() == COLUMNS[key]:
                    count_label = widget.parent().findChild(QtWidgets.QLabel, "count_label")
                    if count_label:
                        count_label.setText(str(count))

    def calculate_percentages(self):
        for col_idx in range(len(self.inspection_data[0])):
            total_checked = self.inspection_data[0][col_idx]
            errors = self.inspection_data[1][col_idx]
            percentage = (errors / total_checked * 100) if total_checked > 0 else 0  # Avoid division by zero
            percentage_item = QtWidgets.QTableWidgetItem(f"{percentage:.2f}%")
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

    def update_quantity(self):
        timeline_idx = self.timeline_combo.currentIndex()
        try:
            quantity = int(self.quantity_input.text())
            self.inspection_data[0][timeline_idx] = quantity
            item = QtWidgets.QTableWidgetItem(str(quantity))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # Make cells read-only
            self.table_widget.setItem(0, timeline_idx, item)
            self.calculate_percentages()
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Invalid Input", "Please enter a valid number for quantity.")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())