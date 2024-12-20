import pymysql

class connectionHandler:
    def __init__(self, host, username, password, database, port):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.port = port

    def criar_conexao(self):
        try:
            conexao = pymysql.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database,
                port=self.port,
                cursorclass=pymysql.cursors.DictCursor  # Opcional, se quiser retorno como dicionário
            )
            return conexao
        except pymysql.MySQLError as e:
            print(f"Erro ao criar conexão com o MySQL: {e}")
            raise
