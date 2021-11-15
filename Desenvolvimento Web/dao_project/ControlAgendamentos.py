from datetime import date, datetime
from bancoDados import Banco
 
class Agendamentos():

    def __init__(self, idAgendamento =0, tipo="", dataCriacao = datetime.now(), dataMarcada = datetime.now(),suspeita ="", descricao="",userId=0,clinicaid=0):
        self.id_agendamentos = idAgendamento
        self.usuario_id = userId
        self.clinica_id = clinicaid
        self.tipo = tipo
        self.data_criacao = dataCriacao
        self.data_marcada = dataMarcada
        self.suspeita = suspeita
        self.descricao = descricao

    def ToString(self):
            return f"Tipo {self.tipo}"

class DAOAgendamentos():
    
    def __init__(self):
        self.banco = Banco()

    def SelectAll(self):    
        return self.banco.ExecutarComando("select * from tb_agendamentos")
        
    def SelectPorId(self, userId):    
        return self.banco.ExecutarComando("select * from tb_agendamentos where usuario_id ==?", parametros=[userId])

    def SelectId(self, agendamentoId):
        return self.banco.ExecutarComando("select * from tb_agendamentos where id_agendamentos ==?", parametros=[agendamentoId])

    def Drop(self, agendamentoId):
        return self.banco.ExecutarComando("delete from tb_agendamentos where id_agendamentos ==?", parametros=[agendamentoId])

    def Update(self, agendamento):
        return self.banco.ExecutarComando("update tb_agendamentos tipo =?, data_criacao=?, data_marcada=?, suspeita=?, descricao=?,clinica_id=? where id_agendamentos =?",
        [agendamento.tipo, agendamento.data_criacao, agendamento.data_marcada, agendamento.suspeita, agendamento.descricao, agendamento.clinica_id, agendamento.id_agendamentos])

    def Insert(self, agendamento):
        return self.banco.ExecutarComando("insert into tb_agendamentos (tipo, data_criacao, data_marcada, suspeita, descricao, usuario_id, clinica_id) values (?, ?, ?, ?, ?, ?, ?)",
        [agendamento.tipo, agendamento.data_criacao, agendamento.data_marcada, agendamento.suspeita, agendamento.descricao, agendamento.usuario_id, agendamento.clinica_id])
