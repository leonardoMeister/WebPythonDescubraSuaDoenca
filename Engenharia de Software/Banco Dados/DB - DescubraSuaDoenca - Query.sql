CREATE DATABASE db_descubra_sua_doenca
GO
USE db_descubra_sua_doenca
GO
CREATE TABLE tb_endereco(
	id_endereco int identity(1,1) not null,
	cidade varchar(30) not null,
	estado varchar(30) not null,
	rua varchar(30)  null,
	numero varchar(10) null,

	primary key (id_endereco),
)
GO
CREATE TABLE tb_usuario (
	id_usuario INT IDENTITY(1,1) NOT NULL,
	nome VARCHAR(50) NOT NULL,
	cpf VARCHAR(14) NOT NULL UNIQUE,
	telefone VARCHAR(14)  NULL,
	email VARCHAR(40) NOT NULL,
	senha VARCHAR(30) NOT NULL,
	data_nascimento DATETIME null,
	tipo_sanguineo varchar(10) null,
	alergia varchar(10)  null,
	endereco_id INT null,

	CONSTRAINT FK_Endereco_usuario FOREIGN KEY (endereco_id) REFERENCES tb_endereco(id_endereco) ON DELETE CASCADE ,

	PRIMARY KEY(id_usuario),
) 
GO
CREATE TABLE tb_doenca(
	id_doenca int identity(1,1) not null,
	nome varchar(30) not null,
	descricao varchar(30) not null,
	gravidade varchar(10) not null,
	tratamento varchar(30) not null,
	sintomas varchar(100) not null,

	primary key(id_doenca),
)
GO
CREATE TABLE tb_doencas_contraidas(
	id_doencas_contraidas INT IDENTITY(1,1) NOT NULL,
	nome VARCHAR(30) NOT NULL,
	data_contracao DATETIME NOT NULL,
	data_cura DATETIME NULL,
	descricao VARCHAR(100) NULL,
	detalhes varchar(100) null,
	gravidade varchar(30) null,
	internacao varchar(30) null,
	sintomas varchar(30) null,

	usuario_id INT not null,
	doenca_id INT null,

	CONSTRAINT FK_Doenca FOREIGN KEY (doenca_id) REFERENCES tb_doenca(id_doenca) ON DELETE CASCADE ,
	CONSTRAINT FK_Usuario_Doencas FOREIGN KEY (usuario_id) REFERENCES tb_usuario(id_usuario) ON DELETE CASCADE ,
	PRIMARY KEY(id_doencas_contraidas),
)
GO
CREATE TABLE tb_clinica(
	id_clinica INT IDENTITY(1,1) NOT NULL,
	nome VARCHAR(30) NOT NULL,
	cnpj VARCHAR(14) NOT NULL,
	telefone VARCHAR(14) NOT NULL,
	endereco VARCHAR(30) NULL,
	responsavel VARCHAR(30) NOT NULL,

	endereco_id INT null,

	CONSTRAINT FK_Endereco_Clinica FOREIGN KEY (endereco_id) REFERENCES tb_endereco(id_endereco) ON DELETE CASCADE ,

	PRIMARY KEY(id_clinica),
)
GO
CREATE TABLE tb_agendamentos(
	id_agendamentos INT IDENTITY(1,1) NOT NULL,
	tipo VARCHAR NOT NULL,
	data_criacao DATETIME not null,
	data_marcada DATETIME NOT NULL,
	suspeita VARCHAR(30) NOT NULL,
	descricao varchar(30) not null,

	usuario_id INT not null,
	clinica_id INT null,

	CONSTRAINT FK_Usuario_agendamentos FOREIGN KEY (usuario_id) REFERENCES tb_usuario(id_usuario) ON DELETE CASCADE ,
	PRIMARY KEY(id_agendamentos),
)
GO
CREATE TABLE tb_laudos(
	id_laudo INT IDENTITY(1,1) NOT NULL,
	data_entrada DATETIME NOT NULL,

	clinica_id INT null,
	usuario_id INT not null,

	CONSTRAINT FK_Usuario_laudo FOREIGN KEY (usuario_id) REFERENCES tb_usuario(id_usuario)  ,
	CONSTRAINT FK_Clinica_laudo FOREIGN KEY (clinica_id) REFERENCES tb_clinica(id_clinica)  ,
)
GO
CREATE TABLE tb_log (
	id_log INT IDENTITY(1,1)  NOT NULL,
	tipo VARCHAR(30)  NOT NULL,
	descricao VARCHAR(30) NOT NULL,
	data_log DATETIME NULL,
	
	usuario_id INT  NULL ,
	PRIMARY KEY(id_log),

	CONSTRAINT FK_Usuario_log FOREIGN KEY (usuario_id) REFERENCES tb_usuario(id_usuario) ON DELETE CASCADE ,
) 
