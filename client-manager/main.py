from database import *

create_table()

while True:
    print("\n1. Add Client")
    print("2. List Clients")
    print("3. Update Client")
    print("4. Delete Client")
    print("5. Exit")

    choice = input("choose: ")

    if choice == "1":
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        add_client(name, email, phone)

    elif choice == "2":
        for client in list_clients():
            print(client)

    elif choice == "3":
        id = input("ID: ")
        name = input("New Name: ")
        email = input("New Email: ")
        phone = input("New Phone: ") 
        update_client(id, name, email, phone)

    elif choice == "4":
        id = input("ID: ")
        delete_client(id)

    elif choice == "5":
        break