import sys
from PySide6 import QtCore, QtWidgets

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QtWidgets.QVBoxLayout(self)

        self.grid_layout = QtWidgets.QGridLayout()
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
            for j in range(3):
                index = i * 3 + j
                label = QtWidgets.QLabel(labels[index])
                input_field = QtWidgets.QLineEdit()
                self.grid_layout.addWidget(label, i * 2, j)
                self.grid_layout.addWidget(input_field, i * 2 + 1, j)
                self.inputs.append(input_field)

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