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
        return self.banco.ExecutarComando("select * from tb_doenca")
        
    def SelectId(self, idDoenca):
        return self.banco.ExecutarComando("select * from tb_doenca where id_doenca == ?", [idDoenca])

    def SelectName(self, nome):
        return self.banco.ExecutarComando("select nome from tb_doenca where nome == ?", [nome])
    
    def SelectPorNome(self, nome):
        nome = "%" + nome + "%"
        return self.banco.ExecutarComando("select * from tb_doenca where nome like ?", [nome])

    def Drop(self, idDoenca):
        return self.banco.ExecutarComando("delete from tb_doenca where id_doenca == ?", [idDoenca])

    def Update(self, doenca):
        return self.banco.ExecutarComando("update tb_doenca set nome = ?, descricao = ?, gravidade = ?, tratamento=?, sintomas =? where nome == ?",[doenca.nome, doenca.descricao,doenca.gravidade,doenca.tratamento,doenca.sintomas,doenca.nome])

    def Insert(self, doenca):
        return self.banco.ExecutarComando("insert into tb_doenca (nome, descricao, gravidade, tratamento, sintomas) values (?, ?, ?, ?, ?)", [doenca.nome,doenca.descricao,doenca.gravidade,doenca.tratamento, doenca.sintomas])