"""
Main function for starting the OHappening application. Run the start command to start the application.

FEATURE LIST
------------                        Started Done
-Project initialization and basics  [X]     [ ]
-Working 352 day calendar           [ ]     [ ]
-Clock                              [ ]     [ ]
-Various timers                     [ ]     [ ]
-Syncing with google calendar       [ ]     [ ]
-Admin UI and tools                 [ ]     [ ]

Last updated: 21.01.2019, Ilmo Salmenperä
"""
import sys
import pkg_resources
import logging

from PyQt5.QtWidgets import QMainWindow, QApplication

class OHappenWindow(QMainWindow):
    """
    Class for containing all functionality in OHappening. The heart of it all.
    """
    def __init__(self, screen_size, debug):
        super().__init__()
        self.initLogging(debug)

        self.logger.info('Initializing OHappenWindow variables')

        OHAPPENING_VERSION = pkg_resources.require("OHappening")[0].version
        self.title = "OHappening {0}".format(OHAPPENING_VERSION)
        self.setWindowTitle(self.title)

        self.logger.info('Initializing OHappenWindowWidgets')

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

def start():
    """
    Starting function for the application. Creates the QApplication and such.
    """
    debug = False

    if len(sys.argv) == 2 and sys.argv[1] == 'DEBUG':
        debug = True

    app = QApplication(sys.argv)
    screen_size = QApplication.desktop().screenGeometry()
    ex = OHappenWindow(screen_size, debug)
    sys.exit(app.exec_())
