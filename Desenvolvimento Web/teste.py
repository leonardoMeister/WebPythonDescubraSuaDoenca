from dao_project.ModelUsuario import DAOUsuario, Usuario
from dao_project.ControlEndereco import DAOEndereco, Endereco,Banco



banco =DAOUsuario()
email = "pedro@gmail.com"
user =   banco.VerificarExistencia(email)
print(user)
"""

banco = DAOUsuario()

user = Usuario(alergia="sem",cpf="12345304500",data_nascimento="20-09-2021",email="pedro@gmail.com",nome="leonardo",senha="nada a ver",telefone="993452356",tipo_sangue="O+",endereco_id=0)

banco.Insert(user=user)
"""