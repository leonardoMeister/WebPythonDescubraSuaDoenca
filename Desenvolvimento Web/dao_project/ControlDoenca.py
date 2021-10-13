from datetime import datetime
from bancoDados import Banco
 
class Doenca():

    def __init__(self):
        self.id_doenca = 0
        self.nome = ""
        self.descricao = ""
        self.gravidade = ""
        self.tratamento =""
        self.sintomas = ""

    def ToString(self):
            return f"Tipo {self.nome}"

class DAODoenca():
    
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