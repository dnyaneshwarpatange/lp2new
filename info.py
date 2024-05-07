class InformationManagementSystem:
    def __init__(self):
        self.information = {}

    def add_information(self, category, key, value):
        if category not in self.information:
            self.information[category] = {}
        self.information[category][key] = value
        print(f"Information '{key}' added successfully to category '{category}'.")

    def retrieve_information(self, category, key):
        if category in self.information and key in self.information[category]:
            return self.information[category][key]
        else:
            return f"Information '{key}' not found in category '{category}'."

    def delete_information(self, category, key):
        if category in self.information and key in self.information[category]:
            del self.information[category][key]
            print(f"Information '{key}' deleted successfully from category '{category}'.")
        else:
            print(f"Information '{key}' not found in category '{category}'.")

    def search_by_category(self, category):
        if category in self.information:
            return self.information[category]
        else:
            return f"No information found in category '{category}'."

# Example usage
ims = InformationManagementSystem()

while True:
    print("\n1. Add Information")
    print("2. Retrieve Information")
    print("3. Delete Information")
    print("4. Search by Category")
    print("5. Exit")
    
    choice = input("\nEnter your choice: ")

    if choice == '1':
        category = input("Enter category: ")
        key = input("Enter key: ")
        value = input("Enter value: ")
        ims.add_information(category, key, value)
    elif choice == '2':
        category = input("Enter category: ")
        key = input("Enter key to retrieve: ")
        print(ims.retrieve_information(category, key))
    elif choice == '3':
        category = input("Enter category: ")
        key = input("Enter key to delete: ")
        ims.delete_information(category, key)
    elif choice == '4':
        category = input("Enter category to search: ")
        print(ims.search_by_category(category))
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")