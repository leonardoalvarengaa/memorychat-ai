import sqlite3

DATABASE = "memorychat.db"


def conectar():
    return sqlite3.connect(DATABASE)



def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS mensagens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT,
            mensagem TEXT,
            data_hora DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    conn.commit()
    conn.close()



def salvar_mensagem(role, mensagem):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO mensagens (role, mensagem) VALUES (?, ?)",
        (role, mensagem),
    )

    conn.commit()
    conn.close()



def carregar_historico():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT role, mensagem FROM mensagens ORDER BY id ASC"
    )

    dados = cursor.fetchall()
    conn.close()

    return dados

def limpar_historico():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM mensagens")

    conn.commit()
    conn.close()