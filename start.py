import sys
import datetime
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox, QTableWidgetItem
from start_ui import Ui_Dialog
import user_data
from widget_manager import widget
import welcome
import addToStock
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["pham"]  # Replace with your MongoDB database name
purchases_collection = db["purchases"]
stock_collection = db["stock"]

# Sets up the UI, connects button clicks to their respective functions
class StartDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.total = 0
        self.welcomeScreen = None
        self.StockScreen = None
        self.setupUI()
        self.refresh_data()

    def setupUI(self):
        self.ui.label_5.setText(user_data.name)
        self.ui.label_5.setStyleSheet(
            "color: white;border-radius: 20px; border-color:rgb(0, 0, 0); background-image: url(:/newPrefix/start2.jpg); font-size: 28pt; text-align:center;")

        self.ui.Signout.clicked.connect(self.signOut)
        self.ui.signup_button_8.clicked.connect(self.addToStock)
        self.ui.signup_button_5.clicked.connect(self.print_report)
        self.ui.ptintOrder.clicked.connect(self.print_receipt)
        self.ui.signup_button_6.clicked.connect(self.search_drug)
        self.ui.addbtn.clicked.connect(self.add_order)
        self.ui.deletebtn.clicked.connect(self.remove_order)

    def refresh_data(self, customer_name=None, drug_name=None):
        self.today_purchases()
        self.low_stock()
        self.load_order(customer_name)
        self.load_stock()

    def today_purchases(self):
        current_date = datetime.date.today()
        self.ui.today.clearContents()
        self.ui.today.setRowCount(0)

        query = {"purchase_date": current_date.strftime("%Y-%m-%d")}
        data = list(purchases_collection.find(query))
        self.ui.today.setRowCount(len(data))
        total = 0

        for row_num, row_data in enumerate(data):
            self.ui.today.insertRow(row_num)
            for col_num, value in row_data.items():
                item = QTableWidgetItem(str(value))
                self.ui.today.setItem(row_num, col_num, item)
                if col_num == "price":
                    total += value

        self.ui.totalHome.setText(str(total))

    def low_stock(self):
        self.ui.missing.clearContents()
        self.ui.missing.setRowCount(0)

        query = {"quantity": {"$lte": 50}}
        data = list(stock_collection.find(query))
        self.ui.missing.setRowCount(len(data))

        for row_num, row_data in enumerate(data):
            self.ui.missing.insertRow(row_num)
            for col_num, value in row_data.items():
                item = QTableWidgetItem(str(value))
                self.ui.missing.setItem(row_num, col_num, item)

    def load_order(self, customer_name, current_date=None):
        if current_date is None:
            current_date = datetime.date.today()

        self.ui.orderTable.clearContents()
        self.ui.orderTable.setRowCount(0)

        query = {"customer_name": customer_name, "purchase_date": current_date.strftime("%Y-%m-%d")}
        data = list(purchases_collection.find(query))
        self.ui.orderTable.setRowCount(len(data))

        for row_num, row_data in enumerate(data):
            self.ui.orderTable.insertRow(row_num)
            for col_num, value in row_data.items():
                item = QTableWidgetItem(str(value))
                self.ui.orderTable.setItem(row_num, col_num, item)

    # Function to record orders in purchases and update stock
    def add_order(self):
        customer_name = self.ui.ordersName.text()
        customer_phone = self.ui.ordersMobile.text()
        drug_name = self.ui.orderName.text()
        quantity = int(self.ui.quantity.text())
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")  # Convert date to a string
        current_time = datetime.datetime.now().strftime("%H:%M:%S")  

        stock_data = stock_collection.find_one({"item_name": drug_name})
        price = stock_data("price", 0) * quantity


        if not stock_data:
            QMessageBox.critical(self, "Error", f"{drug_name} is not available in stock.")
        elif int(stock_data["quantity"]) < quantity:
            QMessageBox.critical(self, "Error",
                                 f"No enough quantity in stock for {drug_name}. Available stock: {stock_data['quantity']}.")
        else:
            price = stock_data("price", 0) * quantity  # Use .get() method
            self.total += price
            self.ui.totalOrders.setText(str(self.total))


            purchase_data = {
                "item_name": drug_name,
                "quantity": quantity,
                "purchase_date": current_date,
                "purchase_time": current_time,
                "customer_name": customer_name,
                "customer_phone": customer_phone,
                "price": price
            }
            purchases_collection.insert_one(purchase_data)

            stock_collection.update_one({"item_name": drug_name}, {"$inc": {"quantity": -quantity}})
            self.refresh_data(customer_name, current_date)
            QMessageBox.information(self, "Success", "Drug added successfully.")
            
            
            
        

    # Function to record orders in purchases and update stock
    def remove_order(self):
        customer_name = self.ui.ordersName.text()
        drug_name = self.ui.orderName.text()
        quantity = int(self.ui.quantity.text())

        purchase_data = purchases_collection.find_one({"customer_name": customer_name, "item_name": drug_name})

        if not purchase_data:
            QMessageBox.critical(self, "Error", f"{drug_name} was not added to the order")
        elif purchase_data["quantity"] < quantity:
            QMessageBox.critical(self, "Error", f"You only added {purchase_data['quantity']} to the order")
        else:
            price = stock_collection.find_one({"item_name": drug_name})["price"]
            remaining_quantity = purchase_data["quantity"] - quantity
            new_price = self.total - quantity * price

            if remaining_quantity == 0:
                purchases_collection.delete_one({"customer_name": customer_name, "item_name": drug_name})
            else:
                purchases_collection.update_one({"customer_name": customer_name, "item_name": drug_name},
                                                {"$set": {"quantity": remaining_quantity, "price": new_price}})

            stock_collection.update_one({"item_name": drug_name}, {"$inc": {"quantity": quantity}})
            self.total -= (price * quantity)
            self.ui.totalOrders.setText(str(self.total))
            self.refresh_data()
            QMessageBox.information(self, "Success", f"{quantity} {drug_name} was removed from the order.")

    # Search for the drugs using user input
    def search_drug(self):
        drug_name = self.ui.ordersName_2.text()
        self.load_stock(drug_name)

    # Retrieves the data from the database
                
    def load_stock(self, drug_name=None):
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)
        query = {}
        if drug_name:
            query = {"item_name": {"$regex": f".*{drug_name}.*"}}
        data = list(stock_collection.find(query))
        self.ui.tableWidget.setRowCount(len(data))
        for row_num, row_data in enumerate(data):
            self.ui.tableWidget.insertRow(row_num)
            for col_num, value in enumerate(row_data.values()):
                item = QTableWidgetItem(str(value))  # Ensure value is converted to a string
                self.ui.tableWidget.setItem(row_num, col_num, item)


    # Opens sign out widget
    def signOut(self):
        self.welcomeScreen = welcome.WelcomeDialog()
        widget.addWidget(self.welcomeScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        QMessageBox.information(self, "Sign out", "Sign Out successful!")

    # Opens add to stock widget
    def addToStock(self):
        self.StockScreen = addToStock.StockDialog()
        widget.addWidget(self.StockScreen)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    # Print report for stock
    def print_report(self):
        QMessageBox.information(self, "Print", "Printing stock report...")

    # Print receipt
    def print_receipt(self):
        QMessageBox.information(self, "Print", "Printing order receipt...")
        self.total = 0
        self.ui.totalOrders.setText(str(self.total))
        self.ui.orderTable.clearContents()
        self.ui.orderTable.setRowCount(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = StartDialog()
    dialog.show()
    sys.exit(app.exec_())
