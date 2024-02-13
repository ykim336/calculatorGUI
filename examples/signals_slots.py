import sys
from functools import partial
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget
)

def greet(name):
    if msgLabel.text():
        msgLabel.setText("")
    else:
        msgLabel.setText(f"Hello Kind Sir Named {name}")
    
app = QApplication([])
window = QWidget()
window.setWindowTitle("Signals and slots")
layout = QVBoxLayout()

button = QPushButton("Greet")
button.clicked.connect(partial(greet, "Yvon"))

layout.addWidget(button)
msgLabel = QLabel("")
layout.addWidget(msgLabel)
window.setLayout(layout)
window.show()
sys.exit(app.exec())