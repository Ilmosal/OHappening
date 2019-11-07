from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel, QTextEdit
from PyQt5.QtCore import Qt

from ohappening.config import *

class EventDescriptorWidget(QFrame):
    """
    Class for the more indepth event descriptions.
    """
    def __init__(self, parent, logger):
        self.logger = logger
        self.logger.info('Creating Event Descriptor Widget')
        super().__init__(parent)
        self.setLineWidth(2)
        self.setContentsMargins(0, 0, 0, 0)
        self.setFixedWidth(800)

        self.event_name_text = "<b>{0}</b>"
        self.event_date_text = "<b>Aika:</b> {0}"
        self.event_adress_text = "<b>Paikka:</b> {0}"
        
        self.event_name = QLabel(self.event_name_text.format("No events"), self)
        self.event_name.setStyleSheet(HEADER_COLORS + EVENT_DESCRIPTION_BORDERS)
        self.event_name.setFont(APPLICATION_FONT)
        self.event_name.setFixedHeight(60)

        self.event_date = QLabel(self.event_date_text.format("-"))
        self.event_date.setStyleSheet(EVENT_DESCRIPTION_LR_BORDERS)
        self.event_date.setFont(APPLICATION_FONT)
        self.event_date.setContentsMargins(6, 6, 6, 6)

        self.event_adress = QLabel(self.event_adress_text.format("-"))
        self.event_adress.setStyleSheet(EVENT_DESCRIPTION_LR_BORDERS)
        self.event_adress.setFont(APPLICATION_FONT)
        self.event_adress.setContentsMargins(6, 6, 6, 6)

        self.event_description = QTextEdit(self)
        self.event_description.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.event_description.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.event_description.setReadOnly(True)
        self.event_description.setFont(APPLICATION_FONT)
        self.event_description.setStyleSheet('background-color: rgb(0, 0, 0, 0%); ' + EVENT_DESCRIPTION_LRB_BORDERS)
        self.event_description.setText("")

        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.layout.addWidget(self.event_name)
        self.layout.addWidget(self.event_date)
        self.layout.addWidget(self.event_adress)
        self.layout.addWidget(self.event_description)

    def scrollText(self):
        """
        Function for scrolling text for events which have more text than the box would fit
        """
        pass

    def setNewEventToDescriptor(self):
        """
        Fetch new event for this descriptor
        """
        self.logger.info('Setting a new event to this descriptor')

        event = self.parent().event_list_widget.getEventDescription()

        if event is None:
            self.event_name.setStyleSheet(ORGANIZATION_COLORS["NULL"] + EVENT_DESCRIPTION_BORDERS)
            self.event_name.setText(self.event_name_text.format(""))
            self.event_date.setText(self.event_date_text.format(""))
            self.event_adress.setText(self.event_adress_text.format(""))
            self.event_description.setText("")
            return

        if not ORGANIZATION_FONT_DARK[event.organizer]:
            self.event_name.setStyleSheet(ORGANIZATION_COLORS[event.organizer] + EVENT_DESCRIPTION_BORDERS + "color: white")
        else:
            self.event_name.setStyleSheet(ORGANIZATION_COLORS[event.organizer] + EVENT_DESCRIPTION_BORDERS)

        self.event_name.setText(self.event_name_text.format(event.name))

        if event.start_date.hour == 0 and event.start_date.minute == 0 and event.start_date.second == 0:
            self.event_date.setText(self.event_date_text.format(event.start_date.strftime("%A %d.%m")))
        else:
            self.event_date.setText(self.event_date_text.format(event.start_date.strftime("%A %d.%m klo %H:%M")))
        self.event_adress.setText(self.event_adress_text.format(event.adress))
        self.event_description.setText(event.description)


