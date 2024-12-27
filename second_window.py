# -*- coding: utf-8 -*-
from PySide import QtCore, QtGui
from functools import partial
from constants import SEW_ERRORS, PRIMARY_COLOR

class SecondWindow(QtGui.QWidget):
    error_count_updated = QtCore.Signal(str, int)

    def __init__(self, station, parent=None):
        super(SecondWindow, self).__init__(parent)
        self.resize(1024, 768)
        self.setWindowTitle(u"Other Sewing Errors {}".format(station))
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
            count_label.setObjectName(key)

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
        if (self.error_counts[key] == 0 and delta == -1) or (self.error_counts[key] == 999 and delta == 1):
            return
        
        self.error_counts[key] += delta
        self.error_counts[key] = max(0, self.error_counts[key])  # Ensure count doesn't go below 0
        self.update_error_labels(key)

        # Emit the signal to notify the main window
        self.error_count_updated.emit(key, delta)

    def update_error_labels(self, key):
        for widget in self.findChildren(QtGui.QWidget):
            if isinstance(widget, QtGui.QLabel) and widget.text() in SEW_ERRORS[key]:
                count_label = widget.parent().findChild(QtGui.QLabel, key)
                if count_label:
                    count_label.setText(str(self.error_counts[key]))