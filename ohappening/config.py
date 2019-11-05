"""
This file contains all necessary configuration information for this project
"""
import json
import os
from PyQt5.QtGui import QFont

from ohappening.misc import getStylesheetGradientString

PROJECT_PATH = os.path.join(os.path.dirname(__file__))

APPLICATION_FONT = QFont('Ubuntu', 20)
TITLE_FONT = QFont('Ubuntu', 40, 75)
CLOCK_FONT = QFont('Ubuntu', 26, 75)

HEADER_COLORS = getStylesheetGradientString([42, 130, 34], [79, 184, 70], [115, 224, 105]) + ";"

ORGANIZATION_COLORS = {
    "merididi": getStylesheetGradientString(*[[47, 54, 181], [30, 36, 138], [7, 10, 74]]) + ";",
    "reso": getStylesheetGradientString(*[[255, 112, 203], [247, 59, 178], [212, 2, 135]]) + ";",
    "synop": getStylesheetGradientString(*[[253, 255, 148], [247, 250, 100], [219, 222, 38]]) + ";",
    "geysir": getStylesheetGradientString(*[[107, 101, 100], [77, 72, 71], [59, 56, 55]]) + ";"
}

EVENT_HEADER_BORDERS_DARK = "border: 2px solid black; border-top-right-radius: 25px;" 
EVENT_HEADER_BORDERS_LIGHT = "color: white;" + EVENT_HEADER_BORDERS_DARK
EVENT_HEADER_ADRESS = "border-left: 2px solid black; border-right: 2px solid black; border-bottom: 2px solid black; border-bottom-right-radius: 25px;"
EVENT_HEADER_DATE = "border-left: 2px solid black; border-right: 2px solid black;"

EVENT_DESCRIPTION_BORDERS = "border: 2px solid black;"
EVENT_DESCRIPTION_LR_BORDERS = "border-left: 2px solid black; border-right: 2px solid black;"
EVENT_DESCRIPTION_LRB_BORDERS = "border-left: 2px solid black; border-right: 2px solid black; border-bottom: 2px solid black;"

MAX_WIDGET_AMOUT = 6

ORGANIZATION_FONT_DARK = {
    "merididi": False,
    "reso": True,
    "synop": True,
    "geysir": False
}

CALENDAR_CONFIG_JSON = json.load(open(PROJECT_PATH + '/credentials/calendars.json', 'r'))

