"""
This module contains all important features of the event class
"""

from PyQt5.QtWidgets import QFrame, QGridLayout, QLabel
from PyQt5.QtCore import Qt

from ohappening.config import *
from ohappening.misc import getStylesheetGradientString

class Event():
    """
    Class Representing an event
    """
    def __init__(self, name, adress, organizer, description, start_date, end_date):
        self.name = name
        self.adress = adress
        self.organizer = organizer
        self.description = description
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return "Event: {0}, {1}, {2}, {4} - {5}\n{3}".format(self.name, self.adress, self.organizer, self.description, self.start_date, self.end_date)

class EventWidget(QFrame):
    """
    Class for representing Event in a simple bar format
    """
    def __init__(self, parent, event):
        super().__init__(parent)
        self.event = event

        layout = QGridLayout(self)
        layout.setAlignment(Qt.AlignLeft)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        name_label = QLabel("  <b>{0}</b>".format(event.name), self)
        if ORGANIZATION_FONT_DARK[event.organizer]:
            name_label.setStyleSheet(ORGANIZATION_COLORS[event.organizer] + EVENT_HEADER_BORDERS_DARK)
        else:
            name_label.setStyleSheet(ORGANIZATION_COLORS[event.organizer] + EVENT_HEADER_BORDERS_LIGHT)
        name_label.setFont(APPLICATION_FONT)
        name_label.setFixedWidth(1000)

        if event.start_date.hour == 0 and event.start_date.minute == 0 and event.start_date.second == 0:
            date_label = QLabel("   " + event.start_date.strftime("%A %d.%m").capitalize(), self)
        else:
            date_label = QLabel("   " + event.start_date.strftime("%A %d.%m klo %H:%M").capitalize(), self)
        date_label.setStyleSheet(EVENT_HEADER_DATE)
        date_label.setFont(APPLICATION_FONT)

        adress_label = QLabel("  {0}".format(event.adress), self)
        adress_label.setStyleSheet(EVENT_HEADER_ADRESS)
        adress_label.setFont(APPLICATION_FONT)

        layout.addWidget(name_label, 0, 0)
        layout.addWidget(date_label, 1, 0)
        layout.addWidget(adress_label, 2, 0)

        self.setLayout(layout)
        self.setFixedSize(1000, 130)
