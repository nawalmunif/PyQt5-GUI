from PANDEM import *
from covid import Covid

class CovidThread(QtCore.QThread):
    CovidSignal = QtCore.pyqtSignal(dict)

    def __init__(self, parent=None):
        super(CovidThread, self).__init__(parent=parent)
        self.covid = Covid()
        self.covid = Covid(source="john_hopkins")

    def run(self):
         while True:
            pakistan_cases = self.covid.get_status_by_country_name("pakistan")
            self.CovidSignal.emit(pakistan_cases)
            QtCore.QThread.sleep(30 * 60)