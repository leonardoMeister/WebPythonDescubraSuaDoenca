from datetime import datetime
from bancoDados import Banco
 
class Doenca():

    def __init__(self, nomeD="",descricaoD="", gravidadeD="0",tratamentoD="",sintomasD="", id=0):
        self.id_doenca = id
        self.nome = nomeD
        self.descricao = descricaoD
        self.gravidade = gravidadeD
        self.tratamento =tratamentoD
        self.sintomas = sintomasD

    def ToString(self):
            return f"Tipo {self.nome}"

class DAODoenca():
    
    def __init__(self):
        self.banco = Banco()

    def SelectAll(self):    
        return self.banco.ExecutarComando("select * from tb_endereco")
        
    def SelectId(self):
        pass

    def SelectName(self, nome):
        return self.banco.ExecutarComando("select nome from tb_doenca where nome == ?", [nome])
    
    def Drop(self):
        pass

    def Update(self):
        pass

    def Insert(self, doenca):
        return self.banco.ExecutarComando("insert into tb_doenca (nome, descricao, gravidade, tratamento, sintomas) values (?, ?, ?, ?, ?)", [doenca.nome,doenca.descricao,doenca.gravidade,doenca.tratamento, doenca.sintomas])