# from datetime import datetime
# from medicine import MedicineManager
# class Inventory:
#     def add_stock(self):
#         med_id = input("Enter Medicine ID:")

#         for medicine in MedicineManager.medicines:
#             if medicine.med_id == med_id:
#                 print(f"current stock:{medicine.quantity}")
#                 add_quantity = int(input("Enter quantity to Add:"))
#                 medicine.quantity += add_quantity
#                 print("stock added successfully.")
#                 print(f"updated Stock:{medicine.quantity}")
#                 return
            
#         print("Medicine not found.")
#     def update_stock(self):
#         med_id = input("Enter Medicine ID:")

#         for medicine in MedicineManager.medicines:
#             if medicine.med_id == med_id:
#                 print(f"current stock:{medicine.quantity}")
#                 new_quantity =int(input("Enter new quantity:"))
#                 medicine.quantity = new_quantity
#                 print("Stock Updated Successfully")
#                 print(f"updated stock:{medicine.quantity}")
#                 return
            
#         print("Medicine Not Found.")
#     def view_stock(self):
#         if not MedicineManager.medicines:
#             print("No medicines available.")
#             return
        
#         print("=" * 85)
#         print(f"{'ID':<10}{'Name':<20}{'Company':<20}{'Price':<10}{'Stock':<10}")
#         print("=" * 85)

#         for medicine in MedicineManager.medicines:
#             print(f"{medicine.med_id:<10}{medicine.name:<20}{medicine.company:<20}{medicine.price:<10}{medicine.quantity:<10}")
    
#         print("=" * 85)
#         # if not MedicineManager.medicines:
#         #     print("No Medicines available.")
#         #     return
#         # print("----Inventory----")
#         # for medicine in MedicineManager.medicines:
#         #     print(f"ID:{medicine.med_id}")
#         #     print(f"Name:{medicine.name}")
#         #     print(f"Company:{medicine.company}")
#         #     print(f"Price:{medicine.price}")
#         #     print(f"Quantity:{medicine.quantity}")
#         #     print(f"Expiry:{medicine.expiry_date}")
#     def low_stock_alert(self):
#         if not MedicineManager.medicines:
#             print("No Medicines available.")
#             return
#         print("+----------+----------------------+----------+")
#         print("| ID       |   Name               | stock    |")
#         print("+----------+----------------------+----------+")
#         found = False
#         for medicine in MedicineManager.medicines:
#             if medicine.quantity < 10:
#                 print(f"| {medicine.med_id:<8} | {medicine.name:<20} | {medicine.quantity:<8} |")
#                 found=True
#         if not found:
#             print("| No low stock medicines found.|")
#         print("+----------+----------------------+----------+")
#     def expired_medicine_alert(self):
#         if not MedicineManager.medicines:
#             print("No medicines available")
#             return
#         today=datetime.today()
#         print("+----------+----------------------+----------------+")
#         print("| ID       | Name                 | Expiry Date    |")
#         print("+----------+----------------------+----------------+")
#         found=False
#         for medicine in MedicineManager.medicines:
#             expiry=datetime.strptime(medicine.expiry_date,"%d-%m-%Y")
#             if expiry<today:
#                 print(f"| {medicine.med_id:<8} | {medicine.name:<20} | {medicine.expiry_date:<14} |")
#                 found=True
#         if not found:
#             print("| No expired medicines found.                  |")
#         print("+----------+----------------------+----------------+")
# if __name__ == "__main__":
#     inventory = Inventory()
#     while True:
#         print("\n===== Inventory Menu =====")
#         print("1. Add Stock")
#         print("2. Update Stock")
#         print("3. View Stock")
#         print("4. Low Stock Alert")
#         print("5. Expired Medicine Alert")
#         print("6. Exit")
#         choice = input("Enter your choice: ")
#         if choice == "1":
#             inventory.add_stock()
#         elif choice == "2":
#             inventory.update_stock()
#         elif choice == "3":
#             inventory.view_stock()
#         elif choice == "4":
#             inventory.low_stock_alert()
#         elif choice == "5":
#             inventory.expired_medicine_alert()
#         elif choice == "6":
#             print("Exiting...")
#             break
#         else:
#             print("Invalid Choice!")
# if __name__ == "__main__":
#     inventory = Inventory()
#     while True:
#         print("\n===== Inventory Menu =====")
#         print("1. Add Stock")
#         print("2. Update Stock")
#         print("3. View Stock")
#         print("4. Low Stock Alert")
#         print("5. Expired Medicine Alert")
#         print("6. Exit")
#         choice = input("Enter your choice: ")
#         if choice == "1":
#             inventory.add_stock()
#         elif choice == "2":
#             inventory.update_stock()
#         elif choice == "3":
#             inventory.view_stock()
#         elif choice == "4":
#             inventory.low_stock_alert()
#         elif choice == "5":from datetime import datetime
from modules.medicine import MedicineManager
from datetime import datetime
class Inventory:
    def add_stock(self):
        med_id = input("Enter Medicine ID: ")
        for medicine in MedicineManager.medicines:
            if medicine.med_id == med_id:
                print(f"Current Stock: {medicine.quantity}")
                add_quantity = int(input("Enter quantity to Add: "))
                medicine.quantity += add_quantity
                print("Stock added successfully.")
                print(f"Updated Stock: {medicine.quantity}")
                return
        print("Medicine not found.")
    def update_stock(self):
        med_id = input("Enter Medicine ID: ")
        for medicine in MedicineManager.medicines:
            if medicine.med_id == med_id:
                print(f"Current Stock: {medicine.quantity}")
                new_quantity = int(input("Enter new quantity: "))
                medicine.quantity = new_quantity
                print("Stock Updated Successfully")
                print(f"Updated Stock: {medicine.quantity}")
                return
        print("Medicine not found.")
    def view_stock(self):
        if not MedicineManager.medicines:
            print("No medicines available.")
            return
        print("=" * 85)
        print(f"{'ID':<10}{'Name':<20}{'Company':<20}{'Price':<10}{'Stock':<10}")
        print("=" * 85)
        for medicine in MedicineManager.medicines:
            print(f"{medicine.med_id:<10}{medicine.name:<20}{medicine.company:<20}{medicine.price:<10}{medicine.quantity:<10}")
        print("=" * 85)
    def low_stock_alert(self):
        if not MedicineManager.medicines:
            print("No Medicines available.")
            return
        print("+----------+----------------------+----------+")
        print("| ID       | Name                 | Stock    |")
        print("+----------+----------------------+----------+")
        found = False
        for medicine in MedicineManager.medicines:
            if medicine.quantity < 10:
                print(f"| {medicine.med_id:<8} | {medicine.name:<20} | {medicine.quantity:<8} |")
                found = True
        if not found:
            print("| No low stock medicines found. |")
        print("+----------+----------------------+----------+")
    def expired_medicine_alert(self):
        if not MedicineManager.medicines:
            print("No Medicines available.")
            return
        today = datetime.today()
        print("+----------+----------------------+----------------+")
        print("| ID       | Name                 | Expiry Date    |")
        print("+----------+----------------------+----------------+")
        found = False
        for medicine in MedicineManager.medicines:
            expiry = datetime.strptime(medicine.expiry, "%d-%m-%Y")
            if expiry < today:
                print(f"| {medicine.med_id:<8} | {medicine.name:<20} | {medicine.expiry:<14} |")
                found = True
        if not found:
            print("| No expired medicines found.                  |")
        print("+----------+----------------------+----------------+")
#             