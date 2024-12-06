from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from mysql.connector import Error

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(865, 620)
        MainWindow.setStyleSheet("""
        QMainWindow {
            background-color: white;
        }
        QPushButton {
            background-color: lightgray;
            border: 1px solid #ccc;
            padding: 5px;
            border-radius: 5px;
        }
        QPushButton:pressed {
            background-color: lightblue;
        }
        QPushButton#Delete_button {
            background-color: lightcoral;
            color: white;
        }
        QPushButton#Delete_button:pressed {
            background-color: red;
        }
        """)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.main_layout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.Title = QtWidgets.QLabel("Skibidi Market", self.centralwidget)
        self.Title.setFont(QtGui.QFont("Comic Sans MS", 30))
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.main_layout.addWidget(self.Title)

        self.input_layout = QtWidgets.QHBoxLayout()
        self.create_input_sections()
        self.main_layout.addLayout(self.input_layout)

        self.button_layout = QtWidgets.QHBoxLayout()
        self.create_buttons()
        self.main_layout.addLayout(self.button_layout)

        self.Database = QtWidgets.QTableWidget()
        self.Database.setColumnCount(6)
        self.Database.setHorizontalHeaderLabels(["Item ID", "Item Name", "Supplier", "Department", "Aisle Location", "Price"])
        self.Database.horizontalHeader().setStretchLastSection(True)
        self.main_layout.addWidget(self.Database)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.connect_to_db()

        self.Add_Button.clicked.connect(self.add_item)
        self.Search_Button.clicked.connect(self.search_item)
        self.Update_Button.clicked.connect(self.update_item)
        self.Clear_Button.clicked.connect(self.clear_inputs)
        self.Delete_button.clicked.connect(self.delete_item)

        self.load_data()

    def create_input_sections(self):
        self.left_layout = QtWidgets.QGridLayout()
        self.Item = QtWidgets.QLabel("Item")
        self.Item_Line = QtWidgets.QLineEdit()
        self.Supplier = QtWidgets.QLabel("Supplier Name")
        self.Supplier_Name_Line = QtWidgets.QLineEdit()
        self.Department = QtWidgets.QLabel("Department")
        self.Department_List = QtWidgets.QComboBox()
        self.Department_List.addItems(["Produce", "Deli", "Bakery", "Meats & Poultry", "Seafood", "Dairy", "Frozen Foods", "Canned & Packaged Goods", "Beverages", "Snacks", "International Foods", "Bulk Foods", "Organic & Natural", "Seasonal Items"])
        self.left_layout.addWidget(self.Item, 0, 0)
        self.left_layout.addWidget(self.Item_Line, 0, 1)
        self.left_layout.addWidget(self.Supplier, 1, 0)
        self.left_layout.addWidget(self.Supplier_Name_Line, 1, 1)
        self.left_layout.addWidget(self.Department, 2, 0)
        self.left_layout.addWidget(self.Department_List, 2, 1)

        self.right_layout = QtWidgets.QGridLayout()
        self.Item_ID = QtWidgets.QLabel("Item ID")
        self.Item_ID_Line = QtWidgets.QLineEdit()
        self.Price = QtWidgets.QLabel("Price")
        self.Price_Line = QtWidgets.QLineEdit()
        self.Aisle_Location = QtWidgets.QLabel("Aisle Location")
        self.Aisle_Location_List = QtWidgets.QComboBox()
        self.Aisle_Location_List.addItems(["A1", "A2", "B1", "B2", "C1", "C2"])
        self.right_layout.addWidget(self.Item_ID, 0, 0)
        self.right_layout.addWidget(self.Item_ID_Line, 0, 1)
        self.right_layout.addWidget(self.Price, 1, 0)
        self.right_layout.addWidget(self.Price_Line, 1, 1)
        self.right_layout.addWidget(self.Aisle_Location, 2, 0)
        self.right_layout.addWidget(self.Aisle_Location_List, 2, 1)

        self.input_layout.addLayout(self.left_layout)
        self.input_layout.addLayout(self.right_layout)

    def create_buttons(self):
        self.Add_Button = QtWidgets.QPushButton("Add")
        self.Search_Button = QtWidgets.QPushButton("Search")
        self.Update_Button = QtWidgets.QPushButton("Update")
        self.Clear_Button = QtWidgets.QPushButton("Clear")
        self.Delete_button = QtWidgets.QPushButton("Delete")
        self.Delete_button.setObjectName("Delete_button")
        self.button_layout.addWidget(self.Add_Button)
        self.button_layout.addWidget(self.Search_Button)
        self.button_layout.addWidget(self.Update_Button)
        self.button_layout.addWidget(self.Clear_Button)
        self.button_layout.addWidget(self.Delete_button)

    def connect_to_db(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",  
                password="1234567",  
                database="test"
            )
            self.cursor = self.conn.cursor()
            print("Connected to MySQL!")
        except Error as e:
            print(f"MySQL Connection Error: {e}")

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Skibidi Market")

    def add_item(self):
        if not self.Item_Line.text() or not self.Price_Line.text() or not self.Item_ID_Line.text():
            QtWidgets.QMessageBox.warning(None, "Input Error", "Item name, Price, and Item ID are required.")
            return
        try:
            query = """
            INSERT INTO items (item_id, item_name, supplier_name, department, aisle_location, price)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            values = (
                self.Item_ID_Line.text(), 
                self.Item_Line.text(),
                self.Supplier_Name_Line.text(),
                self.Department_List.currentText(),
                self.Aisle_Location_List.currentText(),
                self.Price_Line.text(),
            )
            self.cursor.execute(query, values)
            self.conn.commit()
            QtWidgets.QMessageBox.information(None, "Success", "Item added successfully!")
            self.load_data() 
        except Error as e:
            QtWidgets.QMessageBox.critical(None, "Database Error", f"Error: {e}")

    def search_item(self):
        query = "SELECT * FROM items WHERE item_id = %s"
        self.cursor.execute(query, (self.Item_ID_Line.text(),))
        result = self.cursor.fetchone()
        if result:
            self.Item_Line.setText(result[1])
            self.Supplier_Name_Line.setText(result[2])
            self.Department_List.setCurrentText(result[3])
            self.Aisle_Location_List.setCurrentText(result[6])
            self.Price_Line.setText(str(result[5]))
        else:
            QtWidgets.QMessageBox.warning(None, "Not Found", "Item not found!")

    def update_item(self):
        if not self.Item_ID_Line.text():
            QtWidgets.QMessageBox.warning(None, "Input Error", "Item ID is required to update.")
            return

        query = """
        UPDATE items SET item_name=%s, supplier_name=%s, department=%s, aisle_location=%s, price=%s 
        WHERE item_id=%s
        """
        values = (
            self.Item_Line.text(),
            self.Supplier_Name_Line.text(),
            self.Department_List.currentText(),
            self.Aisle_Location_List.currentText(),
            self.Price_Line.text(),
            self.Item_ID_Line.text(), 
        )
        try:
            self.cursor.execute(query, values)
            self.conn.commit()
            QtWidgets.QMessageBox.information(None, "Success", "Item updated successfully!")
            self.load_data()  
        except Error as e:
            QtWidgets.QMessageBox.critical(None, "Database Error", f"Error: {e}")

    def delete_item(self):
        item_id = self.Item_ID_Line.text()  
        if not item_id:
            QtWidgets.QMessageBox.warning(None, "Input Error", "Item ID is required to delete.")
            return
        
        query = "DELETE FROM items WHERE item_id = %s"
        try:
            self.cursor.execute(query, (item_id,))
            self.conn.commit()
            
            if self.cursor.rowcount > 0:
                QtWidgets.QMessageBox.information(None, "Success", "Item deleted successfully!")
            else:
                QtWidgets.QMessageBox.warning(None, "Not Found", "Item ID not found!")
            
            self.load_data()  
        except Error as e:
            QtWidgets.QMessageBox.critical(None, "Database Error", f"Error: {e}")

    def clear_inputs(self):
        self.Item_Line.clear()
        self.Item_ID_Line.clear()
        self.Supplier_Name_Line.clear()
        self.Price_Line.clear()
        self.Department_List.setCurrentIndex(0)
        self.Aisle_Location_List.setCurrentIndex(0)

    def load_data(self):
        try:
            self.cursor.execute("SELECT item_id, item_name, supplier_name, department, aisle_location, price FROM items")
            rows = self.cursor.fetchall()
            self.Database.setRowCount(0)
            for row in rows:
                row_position = self.Database.rowCount()
                self.Database.insertRow(row_position)
                for column, value in enumerate(row):
                    self.Database.setItem(row_position, column, QtWidgets.QTableWidgetItem(str(value)))
        except Error as e:
            print(f"Error loading data: {e}")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
