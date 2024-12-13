import sys
from PySide6 import QtCore, QtWidgets

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QVBoxLayout(self)

        self.grid_layout = QtWidgets.QGridLayout()
        self.grid_layout.setVerticalSpacing(20)  # Adjust vertical spacing between rows
        self.grid_layout.setHorizontalSpacing(10)  # Adjust horizontal spacing between columns
        self.layout.addLayout(self.grid_layout)

        labels = [
            "Ngày kiểm tra",
            "Danh mục kiểm tra",
            "Mã nhà máy",
            "Loại kiểm tra chất lượng",
            "Dây chuyền",
            "Tổng số lượng kiểm tra"
        ]

        self.inputs = []
        for i in range(2):
            for j in range(4):
                index = i * 4 + j
                if index < len(labels):
                    label = QtWidgets.QLabel(labels[index])
                    label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)  # Align label closer to input
                    if labels[index] == "Dây chuyền":
                        input_field = QtWidgets.QComboBox()
                        input_field.addItems(["A", "B", "C", "D", "E", "F"])
                    else:
                        input_field = QtWidgets.QLineEdit()
                    self.grid_layout.addWidget(label, i * 2, j)
                    self.grid_layout.addWidget(input_field, i * 2 + 1, j)
                    self.inputs.append(input_field)

        # Add table section
        self.table_widget = QtWidgets.QTableWidget(3, 9)
        self.table_widget.setHorizontalHeaderLabels([
            "7:30-8:30", "8:30-9:30", "9:30-10:30", "10:30-11:30", "11:30-12:30",
            "13:30-14:30", "14:30-15:30", "15:30-16:30", "16:30-17:30"
        ])
        self.table_widget.setVerticalHeaderLabels([
            "Số hàng cần kiểm", "Số hàng lỗi", "Tỉ lệ lỗi (%)"
        ])

        # Data for the first two rows
        inspection_data = [
            [100, 120, 140, 160, 180, 200, 220, 240, 260],  # Số hàng cần kiểm
            [7, 56, 4, 89, 6, 10, 11, 12, 13]  # Số hàng lỗi
        ]

        # Fill data into the table
        for row_idx, row_data in enumerate(inspection_data):
            for col_idx, value in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(value))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # Make cells read-only
                self.table_widget.setItem(row_idx, col_idx, item)

        # Calculate the percentage for the third row
        for col_idx in range(len(inspection_data[0])):
            total_checked = inspection_data[0][col_idx]
            errors = inspection_data[1][col_idx]
            percentage = (errors / total_checked * 100) if total_checked > 0 else 0  # Avoid division by zero
            percentage_item = QtWidgets.QTableWidgetItem(f"{percentage:.2f}%")
            percentage_item.setTextAlignment(QtCore.Qt.AlignCenter)
            percentage_item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # Make cells read-only
            self.table_widget.setItem(2, col_idx, percentage_item)

        # Automatically resize column width to fit the window
        header = self.table_widget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.layout.insertWidget(1, self.table_widget)


        # Add sewing error section
        sew_errors = {
            "combination_is_marked": "Tổ hợp bị hằn",
            "combination_has_open_grinding": "Tổ hợp bị hở bào mài",
            "unfavorable_sewing_line": "Đường gò không thuận",
            "sewing_thread_error": "Đường may chỉ lỗi",
            "back_height_uneven_misaligned": "Hậu cao thấp, lệch hậu",
            "nay_niry_too_high_unfavorable": "Nây nỷ nhô cao, không thuận",
            "hair_length_uneven_not_yet_shed": "Lông dài ngắn, chưa gảy lông",
            "button_is_loose_tight_reversed_missing": "Khuy Oze lỏng, chặt, ngược, thiếu",
            "edge_is_dented_wrinkled_uneven_length": "Viền móp, nhăn, dài ngắn",
            "stitching_is_missing_loose_tight": "Khâu thiếu, lỏng, chặt",
            "fabric_color_faded_hair_cracked": "Xía miên mất màu, rạn nứt lông",
            "zipper_head_uneven_height": "Đầu khóa, la len cao thấp",
            "shape_line_not_enough_curvature": "Vệt định hình, không đủ độ cong",
            "elastic_thread_not_straight": "Chun rút sợi không thẳng",
            "raw_cow_head_uneven_high_low": "Đầu bò sống lệch, cao thấp",
            "ear_strap_uneven_short_long": "Dây tai dài ngắn, lệch",
            "hole_punched_torn_misaligned_not_clear": "Đục lỗ toét, lệch, không thông",
            "valid_combination_not_flexible": "Hợp lệch xía uyển",
            "fake_stitching_pencil_line_on_form": "May giả chỉ, vạch chì chân phom",
            "back_shaping_knife_insertion_incorrect": "Định hình hậu xỏ dao không đúng",
        }

        row = 4
        col = 0

        for key, value in sew_errors.items():
            block_layout = QtWidgets.QVBoxLayout()

            label = QtWidgets.QLabel(value)
            label.setAlignment(QtCore.Qt.AlignCenter)

            h_layout = QtWidgets.QHBoxLayout()
            decrement_button = QtWidgets.QPushButton("-")
            decrement_button.setStyleSheet("background-color: red; color: white;")
            count_label = QtWidgets.QLabel("0")
            increment_button = QtWidgets.QPushButton("+")
            increment_button.setStyleSheet("background-color: green; color: white;")

            count_label.setAlignment(QtCore.Qt.AlignCenter)
            h_layout.addWidget(decrement_button)
            h_layout.addWidget(count_label)
            h_layout.addWidget(increment_button)

            block_layout.addWidget(label)
            block_layout.addLayout(h_layout)

            block_widget = QtWidgets.QWidget()
            block_widget.setLayout(block_layout)
            block_widget.setStyleSheet("border: 1px solid black; background-color: white;")

            self.grid_layout.addWidget(block_widget, row, col)

            col += 1
            if col == 4:
                col = 0
                row += 1

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())