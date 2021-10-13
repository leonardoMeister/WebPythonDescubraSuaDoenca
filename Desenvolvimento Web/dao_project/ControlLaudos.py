from datetime import datetime
from bancoDados import Banco
 
class Laudo():

    def __init__(self):
        self.id_laudo = 0
        self.clinica_id = 0
        self.usuario_id = 0
        self.data_entrada = datetime.now()
        self.pdf = ""

    def ToString(self):
            return f"ID LAUDO {self.id_laudo}"

class DAODoencasContraidas():
    
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