"""Show card object. Display a text."""
import sys

from PySide6 import QtWidgets
from PySide6.QtCore import QSize, QRect, QPoint, QPointF
from PySide6.QtGui import QPalette, QPaintEvent, QPainter, Qt
from PySide6.QtWidgets import QWidget, QSizePolicy, QLabel


class CardWidget(QWidget):
    def __init__(self, text='', ruby='', parent=None):
        super().__init__(parent)

        # internal data
        self._main_text: str = text
        self._ruby_text: str = ruby

        self.setBackgroundRole(QPalette.Base)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    def sizeHint(self) -> QSize:
        return QSize(200, 160)

    def set_main_text(self, text: str):
        self._main_text = text

    def set_format(self):
        self.main_text_label = QLabel(self, self._main_text)

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self)
        font = painter.font()
        font.setPixelSize(30)
        painter.setFont(font)
        contents_rect = self.contentsRect()
        painter.drawText(contents_rect, Qt.AlignCenter, self._main_text)
        font = painter.font()
        font.setPixelSize(18)
        painter.setFont(font)
        ruby_rect = QRect(0, contents_rect.height()/2-50,
                          contents_rect.width(), contents_rect.height())
        painter.drawText(ruby_rect, Qt.AlignHCenter | Qt.AlignJustify, self._ruby_text)
        pen = painter.pen()
        pen.setStyle(Qt.DotLine)
        painter.setPen(pen)
        painter.drawRoundedRect(contents_rect, 20, 20)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    widget = CardWidget()
    widget.show()

    sys.exit(app.exec())
