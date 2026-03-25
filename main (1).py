import psycopg2

conexao = psycopg2.connect(
    database = "postgres",
    user = "postgres",
    password = " ",
    host = "",
    port = '5432'
)

cursor = conexao.cursor()

cursor.execute("select * from clientes")

data = cursor.fetchall()
for d in data:
    print(d)
    
conexao.close()