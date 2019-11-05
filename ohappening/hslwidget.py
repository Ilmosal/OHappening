from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class HSLWidget(QFrame):
    """
    Class for the HSL information box. Contains updaing information about local hsl bike stop situation and some bus arrival times for local bus stops.
    """
    def __init__(self, parent, logger):
        self.logger = logger
        self.logger.info('Creating HSL Widget')
        super().__init__(parent)
        self.setFrameStyle(QFrame.Box)
        self.setLineWidth(2)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(QLabel('HSLWidget', self))

    def updateHslWidget(self):
        """
        Function for updating the HSL widget
        """
        self.logger.info('Updating hsl widget')
