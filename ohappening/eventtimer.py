from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class EventTimerWidget(QFrame):
    """
    Class for the event timer functionality of the program. This widget contains countdowns to important times set by the users
    """
    def __init__(self, parent, logger):
        self.logger = logger
        self.logger.info('Creating Event Timer Widget')
        super().__init__(parent)
        self.setFrameStyle(QFrame.Box)
        self.setLineWidth(2)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(QLabel('EventTimerWidget', self))
