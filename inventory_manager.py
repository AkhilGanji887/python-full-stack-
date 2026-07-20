import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))
from modules.inventory import Inventory
class InventoryManager:
    def __init__(self):
        self.inventory=Inventory()
    def menu(self):
        while True:
            print("\n===== Inventory Menu =====")
            print("1. Add Stock")
            print("2. Update Stock")
            print("3. View Stock")
            print("4. Low Stock Alert")
            print("5. Expired Medicine Alert")
            print("6. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.inventory.add_stock()
            elif choice == "2":
                self.inventory.update_stock()
            elif choice == "3":
                self.inventory.view_stock()
            elif choice == "4":
                self.inventory.low_stock_alert()
            elif choice == "5":
                self.inventory.expired_medicine_alert()
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid Choice!")
if __name__ == "__main__":
    manager=InventoryManager()
    manager.menu()