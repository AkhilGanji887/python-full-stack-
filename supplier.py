# class Supplier:
#     def __init__(self, supplier_id, name, company, phone, addres):
#         self.supplier_id = supplier_id
#         self.name = name
#         self.company = company
#         self.phone = phone
#         self.address = addres
# class SupplierManager:
#     suppliers = []
#     def add_supplier(self):
#         supplier_id=input("Enter Supplier Id:")
#         name=input("Enter supplier Name:")
#         company=input("Enter company Number:")
#         phone=input("Enter phone Number:")
#         address=input("Enter Address:")
#         supplier=Supplier(supplier_id, name, company, phone, address)
#         SupplierManager.suppliers.append(supplier)
#         print("Supplier added successfully!")
#     def view_supplier(self):
#         if len(SupplierManager.suppliers) == 0:
#             print("No suppliers available.")
#             return
#         print("----supplier----")
#         for supplier in SupplierManager.suppliers:
#             print(f"""
# Supplier ID:{supplier.supplier_id})
# Name       :{supplier.name}
# Company    :{supplier.company}
# Phone      :{supplier.phone}
# Address    :{supplier.address}
# """)
#     def update_supplier(self):
#         supplier_id=input("Enter supplier IDto update:")
#         for supplier in SupplierManager.suppliers:
#             if supplier.supplier_id == supplier_id:
#                 print("Press Enter to keep the current value.")
#                 name=input(f"Enter New Name ({supplier.name}):")
#                 company=input(f"Enter New Company({supplier.company}):")
#                 phone=input(f"Enter New Phone ({supplier.phone}):")
#                 address=input(f"Enter New Adress ({supplier.address}):")
#                 if name:
#                     supplier.name=name
#                 if company:
#                     supplier.company=company
#                 if phone:
#                     supplier.phone=phone
#                 if address:
#                     supplier.address=address
#                 print("Supplier updated successfully!")
#                 return
#         print("supplier not found")
#     def delete_supplier(self):
#         supplier_id=input("Enter Supplier ID to delete:")
#         for supplier in SupplierManager.suppliers:
#             SupplierManager.suppliers.remove(supplier)
#             print("Supplier deleted successfully")
#             return
#         print("Supplier not found")
#     def search_supplier(self):
#         supplier_id=input("Enter Supplier Id to Searh:")
#         for supplier in SupplierManager.suppliers:
#             if supplier.supplier_id == supplier_id:
#                 print("Supplier Details")
#                 print(f"Supplier ID:{supplier.supplier_id}")
#                 print(f"Name       :{supplier.name}")
#                 print(f"Company    :{supplier.company}")
#                 print(f"Phone      :{supplier.phone}")
#                 print(f"Address    :{supplier.address}")
#                 return
            
#             print("Supplier not found.")
# if __name__ == "__main__":
#     sm = SupplierManager()
#     while True:
#         print("\n===== Supplier Management =====")
#         print("1. Add Supplier")
#         print("2. View Supplier")
#         print("3. Update Supplier")
#         print("4. Delete Supplier")
#         print("5. Search Supplier")
#         print("6. Exit")
#         choice = input("Enter your choice: ")
#         if choice == "1":
#             sm.add_supplier()
#         elif choice == "2":
#             sm.view_supplier()
#         elif choice == "3":
#             sm.update_supplier()
#         elif choice == "4":
#             sm.delete_supplier()
#         elif choice == "5":
#             sm.search_supplier()
#         elif choice == "6":
#             print("Exiting...")
#             break
#         else:
#             print("Invalid choice! Please try again.")
class Supplier:
    def __init__(self, supplier_id, name, company, phone, address):
        self.supplier_id = supplier_id
        self.name = name
        self.company = company
        self.phone = phone
        self.address = address
class SupplierManager:
    suppliers = []
    def add_supplier(self):
        supplier_id = input("Enter Supplier ID: ")
        name = input("Enter Supplier Name: ")
        company = input("Enter Company Name: ")
        phone = input("Enter Phone Number: ")
        address = input("Enter Address: ")
        supplier = Supplier(supplier_id, name, company, phone, address)
        SupplierManager.suppliers.append(supplier)
        print("Supplier added successfully!")
    def view_supplier(self):
        if not SupplierManager.suppliers:
            print("No suppliers available.")
            return
        print("----- Supplier List -----")
        for supplier in SupplierManager.suppliers:
            print(f"""
Supplier ID : {supplier.supplier_id}
Name        : {supplier.name}
Company     : {supplier.company}
Phone       : {supplier.phone}
Address     : {supplier.address}
""")
    def update_supplier(self):
        supplier_id = input("Enter Supplier ID to update: ")
        for supplier in SupplierManager.suppliers:
            if supplier.supplier_id == supplier_id:
                print("Press Enter to keep the current value.")
                name = input(f"Enter New Name ({supplier.name}): ")
                company = input(f"Enter New Company ({supplier.company}): ")
                phone = input(f"Enter New Phone ({supplier.phone}): ")
                address = input(f"Enter New Address ({supplier.address}): ")
                if name:
                    supplier.name = name
                if company:
                    supplier.company = company
                if phone:
                    supplier.phone = phone
                if address:
                    supplier.address = address
                print("Supplier updated successfully!")
                return
        print("Supplier not found.")
    def delete_supplier(self):
        supplier_id = input("Enter Supplier ID to delete: ")
        for supplier in SupplierManager.suppliers:
            if supplier.supplier_id == supplier_id:
                SupplierManager.suppliers.remove(supplier)
                print("Supplier deleted successfully!")
                return
        print("Supplier not found.")
    def search_supplier(self):
        supplier_id = input("Enter Supplier ID to Search: ")
        for supplier in SupplierManager.suppliers:
            if supplier.supplier_id == supplier_id:
                print("\nSupplier Details")
                print(f"Supplier ID : {supplier.supplier_id}")
                print(f"Name        : {supplier.name}")
                print(f"Company     : {supplier.company}")
                print(f"Phone       : {supplier.phone}")
                print(f"Address     : {supplier.address}")
                return
        print("Supplier not found.")
if __name__ == "__main__":
    sm = SupplierManager()
    while True:
        print("\n===== Supplier Management =====")
        print("1. Add Supplier")
        print("2. View Supplier")
        print("3. Update Supplier")
        print("4. Delete Supplier")
        print("5. Search Supplier")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            sm.add_supplier()
        elif choice == "2":
            sm.view_supplier()
        elif choice == "3":
            sm.update_supplier()
        elif choice == "4":
            sm.delete_supplier()
        elif choice == "5":
            sm.search_supplier()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")



