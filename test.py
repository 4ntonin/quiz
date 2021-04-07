import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)

root = QWidget()

root.resize(1024, 768)
root.setWindowTitle("Hello world!")
root.show()

sys.exit(app.exec_())
