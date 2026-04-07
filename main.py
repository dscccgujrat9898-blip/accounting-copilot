import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
import webbrowser
import db

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Accounting App - Dashboard")
        self.setGeometry(200, 200, 600, 400)

        layout = QVBoxLayout()

        # Welcome label
        label = QLabel("Welcome to Accounting Dashboard")
        layout.addWidget(label)

        # Reports button
        btn_reports = QPushButton("View Reports")
        btn_reports.clicked.connect(self.open_reports)
        layout.addWidget(btn_reports)

        # Transactions button
        btn_transactions = QPushButton("Add Transaction")
        btn_transactions.clicked.connect(self.open_transactions)
        layout.addWidget(btn_transactions)

        # Inventory button
        btn_inventory = QPushButton("Manage Inventory")
        btn_inventory.clicked.connect(self.open_inventory)
        layout.addWidget(btn_inventory)

        # E-Way Bill portal button
        btn_eway = QPushButton("Open E-Way Bill Portal")
        btn_eway.clicked.connect(self.open_ewaybill)
        layout.addWidget(btn_eway)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_reports(self):
        print("Reports window will open here.")

    def open_transactions(self):
        print("Transactions window will open here.")

    def open_inventory(self):
        print("Inventory window will open here.")

    def open_ewaybill(self):
        webbrowser.open("https://ewaybillgst.gov.in/")

if __name__ == "__main__":
    db.init_db()  # Initialize database
    app = QApplication(sys.argv)
    window = Dashboard()
    window.show()
    sys.exit(app.exec_())
