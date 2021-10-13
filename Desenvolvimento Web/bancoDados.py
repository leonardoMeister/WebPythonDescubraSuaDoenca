import sqlite3
from sqlite3 import Error

class Banco():

    def ConexaoBanco(self):
        caminho = "C:\\Users\\leozi\\Desktop\\Repositorios Python\\WebPythonDescubraSuaDoenca\\Engenharia de Software\\Banco Dados\\BancoDescubraSuaDoenca.db"
        con = None
        try:
            con = sqlite3.connect(caminho)
        except Error as ex:
            print(ex)
            return ex
        return con

    def ExecutarComando(self, sql, parametros=[]):
        try:
            conexao =self.ConexaoBanco() 
            cursor = conexao.cursor()
            
            cursor.execute(sql, parametros)
            conexao.commit()            
            dados = cursor.fetchall()

            print("COMANDO SUCESSO")
            return dados

        except Error as ex:
            print ("ERRO:   "+ str(ex))

        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()