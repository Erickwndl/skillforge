from connection import connectionHandler

# Instância da classe connectionHandler com os parâmetros de conexão
connection_handler = connectionHandler(
    host='autorack.proxy.rlwy.net',
    username='root',
    password='CGwuHntYlbgdGDnqjXcqQmTbAulRrWUv',
    database='railway',
    port=38176
)

# Tente criar uma conexão para testar
try:
    conexao = connection_handler.criar_conexao()
    print("Conexão bem-sucedida!")
except Exception as e:
    print(f"Erro ao conectar: {e}")
