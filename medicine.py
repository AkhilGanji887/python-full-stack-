class Medicine:
    def __init__(self, med_id, name, company, price, quantity, expiry):
        self.med_id = med_id
        self.name = name
        self.company = company
        self.price = price
        self.quantity = quantity
        self.expiry = expiry
class MedicineManager:
    medicines = []
    def add_medicine(self):
        med_id = input("Enter Medicine ID: ")
        name = input("Enter Medicine Name: ")
        company = input("Enter Company Name: ")
        price = float(input("Enter Price: "))
        quantity = int(input("Enter Quantity: "))
        expiry = input("Enter Expiry Date (DD-MM-YYYY): ")
        medicine = Medicine(
            med_id=med_id,
            name=name,
            company=company,
            price=price,
            quantity=quantity,
            expiry=expiry,
        )
        MedicineManager.medicines.append(medicine)
        print("Medicine added successfully!")
    def view_all_medicines(self):
        if not MedicineManager.medicines:
            print("No medicines available.")
            return
        print("\n----- Medicine List -----")
        for medicine in MedicineManager.medicines:
            print(f"Medicine ID   : {medicine.med_id}")
            print(f"Name          : {medicine.name}")
            print(f"Company       : {medicine.company}")
            print(f"Price         : {medicine.price}")
            print(f"Quantity      : {medicine.quantity}")
            print(f"Expiry Date   : {medicine.expiry}")
            print("-" * 30)
    def search_medicine(self):
        med_id = input("Enter Medicine ID to search: ")
        for medicine in MedicineManager.medicines:
            if medicine.med_id == med_id:
                print("\nMedicine Found")
                print(f"Medicine ID   : {medicine.med_id}")
                print(f"Name          : {medicine.name}")
                print(f"Company       : {medicine.company}")
                print(f"Price         : {medicine.price}")
                print(f"Quantity      : {medicine.quantity}")
                print(f"Expiry Date   : {medicine.expiry}")
                return
        print("Medicine Not Found!")
    def update_medicine(self):
        med_id = input("Enter Medicine ID to Update: ")
        for medicine in MedicineManager.medicines:
            if medicine.med_id == med_id:
                medicine.name = input("Enter New Medicine Name: ")
                medicine.company = input("Enter New Company Name: ")
                medicine.price = float(input("Enter New Price: "))
                medicine.quantity = int(input("Enter New Quantity: "))
                medicine.expiry = input("Enter New Expiry Date (DD-MM-YYYY): ")
                print("Medicine Updated Successfully!")
                return
        print("Medicine Not Found!")
    def delete_medicine(self):
        med_id = input("Enter Medicine ID to Delete: ")
        for medicine in MedicineManager.medicines:
            if medicine.med_id == med_id:
                MedicineManager.medicines.remove(medicine)
                print("Medicine Deleted Successfully!")
                return
        print("Medicine Not Found!")
if __name__ == "__main__":
    manager = MedicineManager()
    while True:
        print("\n===== Medicine Management =====")
        print("1. Add Medicine")
        print("2. View All Medicines")
        print("3. Search Medicine")
        print("4. Update Medicine")
        print("5. Delete Medicine")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            manager.add_medicine()
        elif choice == "2":
            manager.view_all_medicines()
        elif choice == "3":
            manager.search_medicine()
        elif choice == "4":
            manager.update_medicine()
        elif choice == "5":
            manager.delete_medicine()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid Choice!")