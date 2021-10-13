from bancoDados import Banco
from datetime import datetime

class Log():

    def __init__(self):
        self.id_log = 0
        self.usuario_id = 0
        self.tipo = ""
        self.descricao = ""
        self.data = datetime.now()

    def ToString(self):
            return f"Tipo {self.tipo}"

class DAOLog():

    def __init__(self):
        self.banco = Banco()

    def SelectAll(self):    
        return self.banco.ExecutarComando("select * from tb_log")
        
    def SelectId(self):
        pass

    def Insert(self):
        return self.banco.ExecutarComando("insert into tb_endereco (cidade, estado, rua, numero) values (?, ?, ?, ?)", ["lages","SC","Miranda","SN"])