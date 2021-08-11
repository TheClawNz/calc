import sys
from PyQt5.QtWidgets import QApplication
from hm import Arayuz

application = QApplication(sys.argv)
hesapMakinesi = Arayuz()

sys.exit(application.exec_())