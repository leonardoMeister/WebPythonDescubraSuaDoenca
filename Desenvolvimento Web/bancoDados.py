import sqlite3
from sqlite3 import Error
from funcoes import Funcoes , LogEnum

class Banco():

    def ConexaoBanco(self):
        caminho = "static\\Banco Dados\\BancoDescubraSuaDoenca.db"
        con = None
        try:
            con = sqlite3.connect(caminho)
            Funcoes.criaLog(LogEnum.INFO, LogEnum.banco, "Conexão banco", "", "Conexão aberta com sucesso")
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
            Funcoes.criaLog(LogEnum.INFO, LogEnum.banco, "COMANDO EXECUTADO BANCO", parametros, sql)
            return dados

        except Error as ex:
            Funcoes.criaLog(LogEnum.WARNING, LogEnum.banco, "ERRO BANCO", parametros, sql)
            print ("ERRO:   "+ str(ex))

        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()