import psycopg2

conn = psycopg2.connect(
    dbname="PostgreSQL",
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
conn.commit()
