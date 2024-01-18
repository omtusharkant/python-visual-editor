import sys
from PyQt5.QtWidgets import *

from visual_wnd import visualwriterwnd


if __name__ == '__main__':
    app = QApplication(sys.argv)

    wnd = visualwriterwnd()

    sys.exit(app.exec_())
