from datetime import datetime
from bancoDados import Banco
 
class DoencasContraidas():

    def __init__(self):
        self.id_doencasContraidas = 0
        self.usuario_id = ""
        self.doenca_id = ""
        self.data_contracao = ""
        self.data_cura = ""
        self.descricao = ""
        self.detalhes = ""
        self.gravidade = ""
        self.internacao = ""
        self.sintomas = ""

    def ToString(self):
            return f"Tipo {self.nome}"

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