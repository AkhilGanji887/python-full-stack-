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
