import pymysql.cursors
from pymysql.cursors import DictCursor
from pymysql import Connection
from dataclasses import dataclass
from pymysql import MySQLError


@dataclass(kw_only=True)
class connectionHandler:
    host: str
    username: str
    password: str
    database: str
    port: int
    cursor: DictCursor = None
    conn: Connection = None

    def __post_init__(self):
        self.conn = self.criar_conexao()
        self.cursor = self.conn.cursor()

    def criar_conexao(self):
        try:
            conexao = pymysql.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database,
                port=self.port,  # Certifique-se de passar a porta corretamente
                cursorclass=pymysql.cursors.DictCursor
            )
            return conexao
        except MySQLError as e:
            print(f"Erro ao conectar ao MySQL: {e}")
            raise 

    def listar_todos(self):
        sql = "SELECT * FROM cursos"
        self.cursor.execute(sql)
        cursos = self.cursor.fetchall()
        return cursos

    def buscar_por_nome(self, nome):
        sql = "SELECT * FROM cursos WHERE nome LIKE %s"
        self.cursor.execute(sql, ('%' + nome + '%',))
        cursos = self.cursor.fetchall()
        return cursos
    
    def buscar_por_categoria(self, categoria):
        sql = "SELECT * FROM cursos WHERE categoria = %s"
        self.cursor.execute(sql, (categoria,))
        cursos = self.cursor.fetchall()
        return cursos
