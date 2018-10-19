from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import  QColor
from PyQt5.QtCore import Qt

large_font_size = 48
medium_font_size = 28
small_font_size = 16

def SetPallete(main_window):
    p = main_window.palette()
    p.setColor(main_window.backgroundRole(), Qt.white)
    main_window.setPalette(p)