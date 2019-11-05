"""
This module contains necessary functions and classes that dont fit elsewhere
"""

def getStylesheetGradientString(bottom, mid, top):
    """
    """
    style_sheet_string = "background: qlineargradient(x1:0, y1:1, x2:0, y2:0, stop: 0 rgb({0}, {1}, {2}), stop: 0.3 rgb({3}, {4}, {5}), stop: 1 rgb({6}, {7}, {8}))"
    return style_sheet_string.format(
            bottom[0],
            bottom[1],
            bottom[2],
            mid[0],
            mid[1],
            mid[2],
            top[0],
            top[1],
            top[2]
            )
