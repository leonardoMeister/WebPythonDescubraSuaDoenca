from bancoDados import Banco
from datetime import datetime
from dao_project.ControlEndereco import Endereco,DAOEndereco

class Usuario():

    def __init__(self, id_usuario=0, nome="", senha="",cpf="", telefone="", email="",data_nascimento=datetime.now(),endereco_id=0,tipo_sangue="",alergia=""):
        self.id_usuario = id_usuario
        self.nome = nome
        self.senha = senha
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.data_nascimento = data_nascimento
        if endereco_id:
            self.endereco = DAOEndereco().SelectId(endereco_id)
        else:
            self.endereco = Endereco()
        self.tipoSague = tipo_sangue
        self.alergia = alergia

    def ToString(self):
            return f"Nome {self.nome}"

class DAOUsuario():

    def __init__(self):
        self.banco = Banco()

    def SelectAll(self):    
        return self.banco.ExecutarComando("select * from tb_usuario")
        
    def SelectId(self, id_user):
        dados = self.banco.ExecutarComando("select * from tb_usuario where id_usuario = ?" , [id_user])
        return Usuario(id_usuario=dados[0][0],nome=dados[0][1],cpf=dados[0][2],telefone=dados[0][3],email=dados[0][4],senha=dados[0][5],data_nascimento=dados[0][6],tipo_sangue=dados[0][7],alergia=dados[0][8],endereco_id=dados[0][9])
 
    def SelectLoginSenha(self, senha, email):
        dados = self.banco.ExecutarComando("select * from tb_usuario where email = ? and senha = ?" , [email , senha])
        if dados:
            return Usuario(id_usuario=dados[0][0],nome=dados[0][1],cpf=dados[0][2],telefone=dados[0][3],email=dados[0][4],senha=dados[0][5],data_nascimento=dados[0][6],tipo_sangue=dados[0][7],alergia=dados[0][8],endereco_id=dados[0][9])
        return False
        
    def VerificarExistencia(self, email):
        dados = self.banco.ExecutarComando("select * from tb_usuario where email = ?", [email])
        if dados:
            return True
        return False
        
    def Drop(self, id_usuario):
        return self.banco.ExecutarComando("delete from tb_usuario where id_usuario = ?" , [id_usuario])

    def Update(self, user):
        return self.banco.ExecutarComando("update tb_usuario set nome = ?, cpf=?, telefone=?, email=?, senha=?, data_nascimento=?, tipo_sanguineo=?, alergia=?, endereco_id=?" , [user.nome,user.cpf,user.telefone,user.email,user.senha,user.data_nascimento,user.tipoSague,user.alergia,user.endereco.id_endereco])

    def Insert(self, user):        
        return self.banco.ExecutarComando("insert into tb_usuario (nome, telefone, email, senha, data_nascimento, tipo_sanguineo, alergia, endereco_id) values (?, ?, ?, ?, ?, ?, ?, ?)", [user.nome,user.telefone,user.email,user.senha,user.data_nascimento,user.tipoSague,user.alergia,user.endereco.id_endereco])
