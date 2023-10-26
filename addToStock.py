import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem, QMessageBox
from addtostock_ui import Ui_Dialog
import pymongo
from widget_manager import widget
from mydatabase import collection


# Sets up the UI, connects button clicks to their respective functions
class StockDialog(Ui_Dialog, QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.start_dialog = None
        self.startstk_dialog = None
        self.ui.back.clicked.connect(self.Back)
        self.ui.signup_button_8.clicked.connect(self.add_drug)
        self.ui.signup_button_9.clicked.connect(self.remove_drug)
        self.load_data()

    def refresh_data(self):
        self.load_data()

    # Retrieves data from the "stock" collection in the MongoDB database
    def load_data(self):
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)
        data = collection.find({}, projection={"_id": 0, "item_name": 1, "provider_name": 1, "quantity": 1, "expire_date": 1})
        data = list(data)
        self.ui.tableWidget.setRowCount(len(data))
        for row_num, doc in enumerate(data):
            self.ui.tableWidget.insertRow(row_num)
            for col_num, value in enumerate(doc.values()):
                item = QTableWidgetItem(str(value))
                self.ui.tableWidget.setItem(row_num, col_num, item)

    # Retrieves drug-related information from the corresponding input fields in the UI and inserts a new document into the "stock" collection in the MongoDB database.
    def add_drug(self):
        drug_name = self.ui.ordersName_2.text()
        provider = self.ui.ordersName_5.text()
        expiry_date = self.ui.ordersName_4.text()
        quantity = self.ui.ordersName_3.text()
        try:
            new_drug = {
                "item_name": drug_name,
                "provider_name": provider,
                "expire_date": expiry_date,
                "quantity": quantity
            }
            collection.insert_one(new_drug)
            self.load_data()
            QMessageBox.information(self, "Added Drug", f"{drug_name} added to stock successfully!")
        except Exception as e:
            QMessageBox.information(self, "Error", f"An error '{e}' occurred while adding {drug_name} to the stock")

    # Removes a drug from the "stock" collection in the MongoDB database based on the provided drug name.
    def remove_drug(self):
        drug_name = self.ui.ordersName_2.text()
        try:
            drug = collection.find_one({"item_name": drug_name})
            if not drug:
                QMessageBox.information(self, "Error", f"{drug_name} does not exist in the stock!")
                return
            collection.delete_one({"item_name": drug_name})
            self.load_data()
            QMessageBox.information(self, "Removed Drug", f"{drug_name} removed from stock successfully!")
        except Exception as e:
            QMessageBox.information(self, "Error", f"An error '{e}' occurred while removing {drug_name} from the stock")

    # Return to the previous widget
    def Back(self):
        last_widget = widget.widget(widget.count() - 1)
        widget.removeWidget(last_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = StockDialog()
    dialog.show()
    sys.exit(app.exec_())
