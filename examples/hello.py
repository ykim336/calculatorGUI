
# S1: Import Necessary Libraries
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

# S2: Define Instance
app = QApplication([])

# S3: Define Window (Widget) & Label
window = QWidget()
window.setWindowTitle("Calculator GUI")
window.setGeometry(100, 100, 280, 80)
helloMsg = QLabel("<h1>Welcome to CalculatorGUI!</h1>", parent=window)
helloMsg.move(60,15)

# S4: Show GUI
window.show()

# S5: Run Event Loop
sys.exit(app.exec())