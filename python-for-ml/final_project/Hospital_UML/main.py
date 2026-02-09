from core.SystemManger import SystemManager 

def main():
    hospital_name = input("Enter Hospital Name to start the system: ")
    manager = SystemManager(hospital_name)

    while True:
        print(f"\n--- {manager.hospital.name} Management System ---")
        print("1. Add Department")
        print("2. Remove Department")
        print("3. Add Patient")
        print("4. Remove Patient")
        print("5. Add Staff")
        print("6. Remove Staff")
        print("7. Exit")
        
        choice = input("Select an option (1-7): ")

        if choice == '1':
            d_name = input("Enter department name: ")
            manager.add_department(d_name)
        
        elif choice == '2':
            d_name = input("Enter department name to remove: ")
            manager.remove_department(d_name)

        elif choice == '3':
            d_name = input("Enter department name: ")
            p_name = input("Enter patient name: ")
            p_age = input("Enter patient age: ")
            p_record = input("Enter medical record: ")
            manager.add_patient(d_name, p_name, p_age, p_record)

        elif choice == '4':
            d_name = input("Enter department name: ")
            p_name = input("Enter patient name to remove: ")
            manager.remove_patient(d_name, p_name)

        elif choice == '5':
            d_name = input("Enter department name: ")
            s_name = input("Enter staff name: ")
            s_age = input("Enter staff age: ")
            s_pos = input("Enter staff position: ")
            manager.add_staff(d_name, s_name, s_age, s_pos)

        elif choice == '6':
            d_name = input("Enter department name: ")
            s_name = input("Enter staff name to remove: ")
            manager.remove_staff(d_name, s_name)

        elif choice == '7':
            print("Exiting System. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()