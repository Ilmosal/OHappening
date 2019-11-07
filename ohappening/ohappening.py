"""
Main module for starting the OHappening application. Run the start function to start the application.

FEATURE LIST
------------                        Started Done
-Project initialization and basics  [X]     [X]
-Working calendar                   [X]     [X]
-Clock                              [X]     [X]
-Various timers                     [X]     [X]
-Syncing with google calendar       [X]     [X]
-HSL widget                         [X]     [ ]
-Event timer Widget                 [ ]     [ ]

Last updated: 11.02.2019, Ilmo Salmenperä
"""
import sys
import pkg_resources
import logging
from datetime import datetime

from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout, QWidget
from PyQt5.QtCore import QTimer

from ohappening.event import Event, EventWidget
from ohappening.eventdescriptor import EventDescriptorWidget
from ohappening.eventlist import EventListWidget
from ohappening.pageheader import PageHeaderWidget
from ohappening.hslwidget import HSLWidget
from ohappening.eventtimer import EventTimerWidget
from ohappening.calendarmanager import CalendarManager
from ohappening.config import CALENDAR_CONFIG_JSON

class OHappenWidget(QWidget):
    """
    Class for containing all widgets for OHappening.
    """
    def __init__(self, parent, logger):
        super().__init__(parent)
        self.logger = logger
        self.logger.info('Creating Grid layout')
        self.layout = QGridLayout(self)
        self.layout.setSpacing(0)

        self.logger.info('Creating Widgets')
        self.page_header_widget = PageHeaderWidget(self, self.logger)
        self.event_list_widget = EventListWidget(self, self.logger)
        self.event_descriptor_widget = EventDescriptorWidget(self, self.logger)
        self.hsl_widget = HSLWidget(self, self.logger)
        self.event_timer_widget = EventTimerWidget(self, self.logger)

        self.logger.info('Creating Managers')
        self.calendar_managers = []

        for calendar_config in CALENDAR_CONFIG_JSON['calendars']:
            self.calendar_managers.append(CalendarManager(calendar_config, logger))

        self.layout.addWidget(self.page_header_widget, 0, 0, 1, 5)
        self.layout.addWidget(self.event_list_widget, 1, 0, 4, 3)
        self.layout.addWidget(self.hsl_widget, 1, 3, 1, 2)
        self.layout.addWidget(self.event_descriptor_widget, 2, 3, 2, 2)
        self.layout.addWidget(self.event_timer_widget, 4, 3, 1, 2)

        self.setLayout(self.layout)

        self.logger.info('Creating Timer')
        start_clock_timer = QTimer(self)
        start_clock_timer.setSingleShot(True)
        start_clock_timer.timeout.connect(self.startMainTimer)
        start_clock_timer.start(1000 * (60 - datetime.now().second))

        self.updateCalendarElements()

    def startMainTimer(self):
        """
        Function for starting the main clock counter
        """
        self.minute_timer = QTimer(self)
        self.minute_timer.timeout.connect(self.minuteChanged)
        self.minute_timer.start(60 * 1000)
        self.minuteChanged()

    def minuteChanged(self):
        """
        Function that will be called every time the minute in this computer changes
        """
        self.logger.info("Minute Change!")
        self.updateCalendarElements()

    def updateCalendarElements(self):
        """
        Function that updates all calendar elements and fetches new elements from the calendars
        """
        events = []
        for calendar in self.calendar_managers:
            events.extend(calendar.fetchEvents())

        self.page_header_widget.updatePageHeader()
        self.event_list_widget.updateEvents(events)
        self.event_descriptor_widget.setNewEventToDescriptor()
        self.hsl_widget.updateHslWidget()

class OHappenWindow(QMainWindow):
    """
    Class for containing all functionality in OHappening. The heart of it all.
    """
    def __init__(self, screen_size, debug):
        super().__init__()
        self.initLogging(debug)

        self.setStyleSheet('background-color : white')

        self.logger.info('Initializing OHappenWindow variables')
        OHAPPENING_VERSION = pkg_resources.require("OHappening")[0].version
        self.title = "OHappening {0}".format(OHAPPENING_VERSION)
        self.setWindowTitle(self.title)

        self.logger.info('Adding OHappenWidget to MainWindow')
        self.setCentralWidget(OHappenWidget(self, self.logger))
        self.centralWidget().layout.setContentsMargins(0, 0, 0, 0)

        self.logger.info('Program initialized. Showing fullscreen')
        self.showFullScreen()

    def initLogging(self, debug):
        """
        Initialize all logging related stuff.
        """
        self.logger = logging.Logger('OHappening Log')

        ch = logging.StreamHandler()

        if debug:
            self.logger.setLevel(logging.DEBUG)
            ch.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.INFO)
            ch.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
        self.logger.debug("Logger initialized") 

def start(debug = False):
    """
    Starting function for the application. Creates the QApplication and such.
    Setting debug to True will enable debugging logs.
    """
    if len(sys.argv) == 2 and sys.argv[1] == 'DEBUG':
        debug = True

    app = QApplication(sys.argv)
    screen_size = QApplication.desktop().screenGeometry()
    ex = OHappenWindow(screen_size, debug)
    sys.exit(app.exec_())

if __name__ == "__main__":
    start()
