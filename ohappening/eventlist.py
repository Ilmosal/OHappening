from PyQt5.QtWidgets import QFrame, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

from ohappening.event import EventWidget
from ohappening.config import MAX_WIDGET_AMOUT

class EventListWidget(QFrame):
    """
    Class for the event list of the application. This class lists the next occurring events in the calendars.
    """
    def __init__(self, parent, logger):
        self.logger = logger
        self.logger.info('Creating Event List Widget')
        super().__init__(parent)
        self.setFrameStyle(QFrame.Box)
        self.setLineWidth(2)

        self.event_counter = 0
        self.events = []

        self.layout = QVBoxLayout(self)

    def updateEvents(self, events):
        """
        Function for updating Event List Widget with events
        """
        self.logger.info('Updating all events')
        self.clearChildren()
        self.events = events

        for e in self.events:
            self.logger.debug(e)

        self.events.sort(key = lambda x: x.start_date)

        counter = 0

        for event in self.events:
            e_widget = EventWidget(self, event)    
            self.layout.addWidget(e_widget)
            counter += 1
            if counter == MAX_WIDGET_AMOUT:
                break

    def clearChildren(self):
        """
        Function for clearing all child objects
        """
        while self.layout.takeAt(0):
            child = self.layout.takeAt(0)
            del child

        self.events.clear()

    def getEventDescription(self):
        """
        Function for getting a single event for the event description. This event will be one of the first 5 events
        """
        if len(self.events) <= self.event_counter:
            return None

        event = self.events[self.event_counter]
        self.event_counter = (self.event_counter + 1) % MAX_WIDGET_AMOUT
        return event
