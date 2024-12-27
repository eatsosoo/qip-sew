# -*- coding: utf-8 -*-
import sys
import yaml
import logging
from functools import partial
from PySide import QtCore, QtGui
from PySide.QtGui import QFontDatabase
from datetime import datetime
from constants import HORIZONTAL_HEADERS, VERTICAL_HEADERS, COLUMNS, SEW_ERRORS, PRIMARY_COLOR, DANGER_COLOR, STYLE_SCROLLBAR
from main_window import MainWindow

with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)
STATION = config["STATION"]

if __name__ == "__main__":
    app = QtGui.QApplication([])
    first_window = MainWindow(STATION)
    first_window.show()
    sys.exit(app.exec_())