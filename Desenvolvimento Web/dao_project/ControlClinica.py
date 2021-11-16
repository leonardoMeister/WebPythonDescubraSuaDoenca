from bancoDados import Banco
 
class Clinica():

    def __init__(self, id = 0, enderecoId =0, nome="", cnpj="", telefone="", responsavel =""):
        self.id_clinica = id
        self.endereco_id = enderecoId
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.responsavel = responsavel

    def ToString(self):
            return f"Tipo {self.tipo}"

class DAOClinica():
    
    def __init__(self):
        self.banco = Banco()

    def SelectAll(self):    
        return self.banco.ExecutarComando("select * from tb_clinica")
        
    def selectName(self, nome):
        return self.banco.ExecutarComando("select * from tb_clinica where nomeFantasia == ?", [nome])
    
    def SelectId(self, clinicaId):
        return self.banco.ExecutarComando("select * from tb_clinica where id_clinica == ?",[clinicaId])

    def Drop(self, clinicaId):
        return self.banco.ExecutarComando("delete from tb_clinica where id_clinica == ?", [clinicaId])

    def Update(self):
        pass

    def Insert(self):
        pass