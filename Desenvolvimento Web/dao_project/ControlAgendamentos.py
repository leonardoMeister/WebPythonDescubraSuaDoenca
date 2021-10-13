from datetime import datetime
from bancoDados import Banco
 
class Agendamentos():

    def __init__(self):
        self.id_agendamentos = 0
        self.usuario_id = 0
        self.clinica_id = 0
        self.tipo = ""
        self.data_criacao = datetime.now()
        self.data_marcada = datetime.now()
        self.suspeita = ""
        self.descricao = ""

    def ToString(self):
            return f"Tipo {self.tipo}"

class DAOAgendamentos():
    
    def __init__(self):
        self.banco = Banco()

    def SelectAll(self):    
        return self.banco.ExecutarComando("select * from tb_endereco")
        
    def SelectId(self):
        pass

    def Drop(self):
        pass

    def Update(self):
        pass

    def Insert(self):
        return self.banco.ExecutarComando("insert into tb_endereco (cidade, estado, rua, numero) values (?, ?, ?, ?)", ["lages","SC","Miranda","SN"])