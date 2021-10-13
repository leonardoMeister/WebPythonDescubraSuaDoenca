from bancoDados import Banco
 
class Clinica():

    def __init__(self):
        self.id_clinica = 0
        self.endereco_id = 0
        self.nome = ""
        self.cnpj = ""
        self.telefone = ""
        self.responsavel = ""

    def ToString(self):
            return f"Tipo {self.tipo}"

class DAOClinica():
    
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