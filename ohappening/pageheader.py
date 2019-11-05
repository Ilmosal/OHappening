from datetime import datetime

from PyQt5.QtWidgets import QFrame, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor, QLinearGradient, QBrush

from ohappening.misc import getStylesheetGradientString
from ohappening.config import TITLE_FONT, CLOCK_FONT

class PageHeaderWidget(QFrame):
    """
    Class for the top header of the ohappening widget. Contains a clock and a title text.
    """
    TOP_COLOR = [167, 164, 247]
    MID_COLOR = [106, 104, 189]
    BOTTOM_COLOR = [87, 86, 117]

    def __init__(self, parent, logger):
        self.logger = logger
        self.logger.info('Creating Page Header Widget')

        super().__init__(parent)
        self.setFrameStyle(QFrame.Box)
        self.setLineWidth(2)
        self.setFixedHeight(100)
        self.setStyleSheet(getStylesheetGradientString(self.BOTTOM_COLOR, self.MID_COLOR, self.TOP_COLOR))

        self.layout = QHBoxLayout(self)
        label = QLabel('OHappening', self)
        label.setStyleSheet('background: rgb(0, 0, 0, 0%)')
        label.setFont(TITLE_FONT)

        self.clock_widget = QLabel('{0} - {1}:{2}'.format(datetime.now().date(), datetime.now().hour, datetime.now().minute), self)
        self.clock_widget.setStyleSheet('background: rgb(0, 0, 0, 0%)')
        self.clock_widget.setFixedWidth(300)
        self.clock_widget.setFont(CLOCK_FONT)

        self.layout.addWidget(label)
        self.layout.addWidget(self.clock_widget)

    def updatePageHeader(self):
        """
        Update Page Header Elements aka. clock
        """
        self.clock_widget.setText('{0} - {1:02d}:{2:02d}'.format(datetime.now().date(), datetime.now().hour, datetime.now().minute))

