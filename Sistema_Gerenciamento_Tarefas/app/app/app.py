import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="RM95177",
    password="210104",
    host="db",  # Nome do serviço do banco de dados definido no docker-compose.yml
    port=5432  # Porta padrão do PostgreSQL
)

cur = conn.cursor()

cur.execute("""
    CREATE TABLE tarefas (
        id SERIAL PRIMARY KEY,
        titulo VARCHAR(255),
        descricao VARCHAR(255)
    )
""")
conn.commit()  # Confirmar a transação


cur.execute("SELECT * FROM tarefas")

cur.execute("SELECT * FROM tarefas")
rows = cur.fetchall()  # Obter todos os resultados da consulta
for row in rows:
    print(row)

cur.execute("INSERT INTO tarefas (titulo, descricao) VALUES (%s, %s)", (valor1, valor2))
conn.commit()  # Confirmar a transação

cur.execute("UPDATE tarefas SET titulo = %s WHERE descricao = %s", (novo_valor1, valor2))
conn.commit()  # Confirmar a transação

cur.execute("DELETE FROM tarefas WHERE titulo = %s", (valor1,))
conn.commit()  # Confirmar a transação

cur.close()
conn.close()






