import sqlite3

def connect():
    return sqlite3.connect("clientes.db")

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_client(name, email, phone):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO CLIENTS (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
    conn.commit()
    conn.close()

def list_clients():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients")
    clients = cursor.fetchall()
    conn.close()
    return clients

def update_client(id, name, email, phone):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE clients SET name=?, email=?, phone=? WHERE id=?", (name, email, phone, id))
    conn.commit()
    conn.close()

def delete_client(id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clients WHERE id=?", (id,))
    conn.commit()
    conn.close()