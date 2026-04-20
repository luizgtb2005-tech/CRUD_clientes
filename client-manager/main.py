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
        
        if not name or not email:
            print("⚠️ Nome e email são obrigatórios!")
            continue
        add_client(name, email, phone)
        print("✅ cliente adicionado com sucesso!!")

    elif choice == "2":
        clients = list_clients()

        if not clients:
            print("📭 Nenhum cliente cadastrado.")
        else:
            for client in clients:
                print(f"""
    ID: {client[0]}
    Nome: {client[1]}
    Email: {client[2]}
    Telefone: {client[3]}
-------------------------
""")

    elif choice == "3":
        id = int(input("ID: "))
        name = input("New Name: ")
        email = input("New Email: ")
        phone = input("New Phone: ")

        update_client(id, name, email, phone)
        print("✏️ Cliente atualizado com sucesso!!")

    elif choice == "4":
        id = int(input("ID: "))

        confirm = input("Tem certeza que deseja deletar? (s/n):")
        
        if confirm.lower() == "s":
            delete_client(id)
            print("🗑️ Cliente removido com sucesso!!")

    elif choice == "5":
        break