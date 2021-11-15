--
-- File generated with SQLiteStudio v3.3.2 on ter nov 9 15:56:14 2021
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: tb_agendamento
CREATE TABLE tb_agendamento (
    id_agendamento        INTEGER      PRIMARY KEY AUTOINCREMENT
                                       NOT NULL,
    dataConsulta          DATETIME,
    dataUltimaModificação DATETIME,
    suspeita              VARCHAR (40),
    categoria             VARCHAR (50),
    urgencia              VARCHAR (30),
    meioAtendimento       VARCHAR (30),
    clinica_id            INTEGER      CONSTRAINT fk_clinica_id REFERENCES tb_clinica (id_clinica) ON DELETE SET NULL
                                                                                                   ON UPDATE NO ACTION,
    descricao             VARCHAR (70) 
);


-- Table: tb_agendamentos
CREATE TABLE tb_agendamentos (
    id_agendamentos INTEGER      PRIMARY KEY AUTOINCREMENT
                                 NOT NULL,
    tipo            VARCHAR (1)  NOT NULL
                                 COLLATE NOCASE,
    data_criacao    DATETIME     NOT NULL,
    data_marcada    DATETIME     NOT NULL,
    suspeita        VARCHAR (30) NOT NULL
                                 COLLATE NOCASE,
    descricao       VARCHAR (30) NOT NULL
                                 COLLATE NOCASE,
    usuario_id      INTEGER      NOT NULL,
    clinica_id      INTEGER,
    FOREIGN KEY (
        usuario_id
    )
    REFERENCES tb_usuario (id_usuario) 
);


-- Table: tb_clinica
CREATE TABLE tb_clinica (
    id_clinica   INTEGER      PRIMARY KEY AUTOINCREMENT
                              NOT NULL,
    nomeFantasia VARCHAR (40) NOT NULL
                              COLLATE NOCASE,
    cnpj         VARCHAR (14) NOT NULL
                              COLLATE NOCASE,
    telefone     VARCHAR (14) NOT NULL
                              COLLATE NOCASE,
    endereco     VARCHAR (30) COLLATE NOCASE,
    responsavel  VARCHAR (30) NOT NULL
                              COLLATE NOCASE,
    endereco_id  INTEGER,
    contato      VARCHAR (15),
    FOREIGN KEY (
        endereco_id
    )
    REFERENCES tb_endereco (id_endereco) 
);


-- Table: tb_doenca
CREATE TABLE tb_doenca (
    id_doenca  INTEGER       PRIMARY KEY AUTOINCREMENT
                             NOT NULL,
    nome       VARCHAR (30)  NOT NULL
                             COLLATE NOCASE,
    descricao  VARCHAR (200) NOT NULL
                             COLLATE NOCASE,
    gravidade  VARCHAR (20)  NOT NULL
                             COLLATE NOCASE,
    tratamento VARCHAR (200) NOT NULL
                             COLLATE NOCASE,
    sintomas   VARCHAR (100) NOT NULL
                             COLLATE NOCASE
);

INSERT INTO tb_doenca (id_doenca, nome, descricao, gravidade, tratamento, sintomas) VALUES (4, 'Gripe', 'É uma doença que acomete principalmente as vias aéreasaéreasaéreas', 'Normal', 'tomar remédios necessários para o seu tratamentotratamentotratamentotratamento', 'Seus sintomas são tosse, espirros e coriza, febre e também dor de cabeça.');

-- Table: tb_doencas_contraidas
CREATE TABLE tb_doencas_contraidas (
    id_doencas_contraidas INTEGER       PRIMARY KEY AUTOINCREMENT
                                        NOT NULL,
    nome                  VARCHAR (30)  NOT NULL
                                        COLLATE NOCASE,
    data_contracao        DATETIME      NOT NULL,
    data_cura             DATETIME,
    descricao             VARCHAR (100) COLLATE NOCASE,
    detalhes              VARCHAR (100) COLLATE NOCASE,
    gravidade             VARCHAR (30)  COLLATE NOCASE,
    internacao            VARCHAR (30)  COLLATE NOCASE,
    sintomas              VARCHAR (30)  COLLATE NOCASE,
    usuario_id            INTEGER       NOT NULL,
    doenca_id             INTEGER,
    FOREIGN KEY (
        usuario_id
    )
    REFERENCES tb_usuario (id_usuario),
    FOREIGN KEY (
        doenca_id
    )
    REFERENCES tb_doenca (id_doenca) 
);


-- Table: tb_endereco
CREATE TABLE tb_endereco (
    id_endereco INTEGER      PRIMARY KEY AUTOINCREMENT
                             NOT NULL,
    cidade      VARCHAR (50) NOT NULL
                             COLLATE NOCASE,
    estado      VARCHAR (2)  NOT NULL
                             COLLATE NOCASE,
    rua         VARCHAR (50) COLLATE NOCASE,
    numero      VARCHAR (10) COLLATE NOCASE
);

INSERT INTO tb_endereco (id_endereco, cidade, estado, rua, numero) VALUES (0, '', '', '', '');
INSERT INTO tb_endereco (id_endereco, cidade, estado, rua, numero) VALUES (2, 'monte', 'SC', 'Estrada', '10003');
INSERT INTO tb_endereco (id_endereco, cidade, estado, rua, numero) VALUES (3, 'monte', 'SC', 'Estrada', '10002');
INSERT INTO tb_endereco (id_endereco, cidade, estado, rua, numero) VALUES (4, 'lages', 'SC', 'Miranda', 'SN');
INSERT INTO tb_endereco (id_endereco, cidade, estado, rua, numero) VALUES (5, 'Blumenau', 'SC', 'Praia', '1024');
INSERT INTO tb_endereco (id_endereco, cidade, estado, rua, numero) VALUES (10, 'jaguarada', 'ad', 'rua', '11143');
INSERT INTO tb_endereco (id_endereco, cidade, estado, rua, numero) VALUES (11, 'cidade', 'ES', 'RUA', '33323');
INSERT INTO tb_endereco (id_endereco, cidade, estado, rua, numero) VALUES (12, 'Monte Carlo', 'SP', '21 de julho', '19923');
INSERT INTO tb_endereco (id_endereco, cidade, estado, rua, numero) VALUES (13, 'Monte Carlo', 'SP', '21 de julho', '19923');
INSERT INTO tb_endereco (id_endereco, cidade, estado, rua, numero) VALUES (14, 'Monte Carlo', 'SP', '21 de julho', '19923');
INSERT INTO tb_endereco (id_endereco, cidade, estado, rua, numero) VALUES (15, 'cidade', 'SC', 'asd', '23422');
INSERT INTO tb_endereco (id_endereco, cidade, estado, rua, numero) VALUES (16, 'cidade', 'SC', 'asd', '44423');
INSERT INTO tb_endereco (id_endereco, cidade, estado, rua, numero) VALUES (17, 'Monte Carlo', 'SP', '21 de julho', '19923');
INSERT INTO tb_endereco (id_endereco, cidade, estado, rua, numero) VALUES (18, 'Monte Carlo', 'SP', '21 de julho', '19923');
INSERT INTO tb_endereco (id_endereco, cidade, estado, rua, numero) VALUES (19, 'Monte Castelos', 'SP', '21 de julho', '19923');
INSERT INTO tb_endereco (id_endereco, cidade, estado, rua, numero) VALUES (20, 'Monte Castelo', 'SP', '21 de julho', '19923');
INSERT INTO tb_endereco (id_endereco, cidade, estado, rua, numero) VALUES (21, 'Monte Carlo', 'SP', '21 de julho', '19923');
INSERT INTO tb_endereco (id_endereco, cidade, estado, rua, numero) VALUES (22, 'Monte Castelo', 'SC', 'Estrada nova', '19923');

-- Table: tb_laudos
CREATE TABLE tb_laudos (
    id_laudo     INTEGER  NOT NULL,
    data_entrada DATETIME NOT NULL,
    clinica_id   INTEGER,
    usuario_id   INTEGER  NOT NULL,
    FOREIGN KEY (
        clinica_id
    )
    REFERENCES tb_clinica (id_clinica),
    FOREIGN KEY (
        usuario_id
    )
    REFERENCES tb_usuario (id_usuario) 
);


-- Table: tb_usuario
CREATE TABLE tb_usuario (
    id_usuario      INTEGER       PRIMARY KEY AUTOINCREMENT
                                  NOT NULL,
    nome            VARCHAR (50)  NOT NULL
                                  COLLATE NOCASE,
    cpf             VARCHAR (14),
    telefone        VARCHAR (14)  COLLATE NOCASE,
    email           VARCHAR (40)  NOT NULL
                                  COLLATE NOCASE,
    senha           VARCHAR (200) NOT NULL
                                  COLLATE NOCASE,
    data_nascimento DATETIME,
    tipo_sanguineo  VARCHAR (10)  COLLATE NOCASE,
    alergia         VARCHAR (30)  COLLATE NOCASE,
    endereco_id     INTEGER,
    FOREIGN KEY (
        endereco_id
    )
    REFERENCES tb_endereco (id_endereco) 
);

INSERT INTO tb_usuario (id_usuario, nome, cpf, telefone, email, senha, data_nascimento, tipo_sanguineo, alergia, endereco_id) VALUES (4, 'leonardo', '333.444.333.22', '(22)2222-33333', 'jacare@gmail.com', '7e3759aa1c6f94082beed27930be292d3207e5b5e3e5bab2a5eacf4b38053a54', '2021-10-08 13:14:56.123145', 'O-', 'Amendoas', 0);
INSERT INTO tb_usuario (id_usuario, nome, cpf, telefone, email, senha, data_nascimento, tipo_sanguineo, alergia, endereco_id) VALUES (6, 'leonardo', '222.222.222.22', '(22)2222-33333', 'pedro@gm', '7e3759aa1c6f94082beed27930be292d3207e5b5e3e5bab2a5eacf4b38053a54', '2021-10-08 13:16:50.039345', 'O-', 'Amendoas', 19);
INSERT INTO tb_usuario (id_usuario, nome, cpf, telefone, email, senha, data_nascimento, tipo_sanguineo, alergia, endereco_id) VALUES (7, 'leonardo', '222.333.333.22', '(22)2222-33333', 'pedro@gmail.c', '7e3759aa1c6f94082beed27930be292d3207e5b5e3e5bab2a5eacf4b38053a54', '2021-10-08 13:21:44.245479', 'O-', 'Amendoas', NULL);
INSERT INTO tb_usuario (id_usuario, nome, cpf, telefone, email, senha, data_nascimento, tipo_sanguineo, alergia, endereco_id) VALUES (8, 'asd', '555.444.555.55', '(22)2222-33333', 'pedro@asd', '7e3759aa1c6f94082beed27930be292d3207e5b5e3e5bab2a5eacf4b38053a54', '2021-10-08 13:30:26.046035', 'O-', 'Medicamentos', 0);
INSERT INTO tb_usuario (id_usuario, nome, cpf, telefone, email, senha, data_nascimento, tipo_sanguineo, alergia, endereco_id) VALUES (9, 'leonardo', '332.443.223.43', '(47)9923-98644', 'leandro@gmail.com', '7e3759aa1c6f94082beed27930be292d3207e5b5e3e5bab2a5eacf4b38053a54', '2021-10-08 15:49:29.193297', 'O-', 'Medicamentos', 0);
INSERT INTO tb_usuario (id_usuario, nome, cpf, telefone, email, senha, data_nascimento, tipo_sanguineo, alergia, endereco_id) VALUES (10, 'leonardo', '111.231.234.54', '(47)9923-98644', 'pedro@gmail.comm', '58bf01092e67681f4e172ed9a5e99907a95e045a10acebf1f5800e2f3137c84e', '2021-10-13 12:25:01.753256', 'O+', 'Amendoas', 0);
INSERT INTO tb_usuario (id_usuario, nome, cpf, telefone, email, senha, data_nascimento, tipo_sanguineo, alergia, endereco_id) VALUES (11, 'leo', '123.321.123.23', '(47)9923-98644', 'leo@gma.com', 'd0ecbc43ac4f980937d2992b3908ae8b7ea548cfe0750e3a0b97532c95adfd45', '2021-10-13 12:25:01.753256', 'O+', 'Medicamentos', 0);
INSERT INTO tb_usuario (id_usuario, nome, cpf, telefone, email, senha, data_nascimento, tipo_sanguineo, alergia, endereco_id) VALUES (12, 'leonardoaaa', '111.111.111.11', '(47)9923-98644', 'leonardoa@gmail.com', '7e3759aa1c6f94082beed27930be292d3207e5b5e3e5bab2a5eacf4b38053a54', '2021-10-28 20:38:24.322705', 'O+', 'Medicamentos', 0);
INSERT INTO tb_usuario (id_usuario, nome, cpf, telefone, email, senha, data_nascimento, tipo_sanguineo, alergia, endereco_id) VALUES (13, 'leonardo', '123.123.123.12', '(47)9923-98644', 'leonardo@gmail', '7e3759aa1c6f94082beed27930be292d3207e5b5e3e5bab2a5eacf4b38053a54', '2021-11-02 12:41:24.018117', 'O+', 'Amendoas', 21);
INSERT INTO tb_usuario (id_usuario, nome, cpf, telefone, email, senha, data_nascimento, tipo_sanguineo, alergia, endereco_id) VALUES (14, 'leonardo', '339.239.555.44', '(47)9923-98644', 'jaja@gmail', '7e3759aa1c6f94082beed27930be292d3207e5b5e3e5bab2a5eacf4b38053a54', '2021-11-02 12:44:05.929782', 'O+', 'Amendoas', 20);
INSERT INTO tb_usuario (id_usuario, nome, cpf, telefone, email, senha, data_nascimento, tipo_sanguineo, alergia, endereco_id) VALUES (15, 'leonardo', NULL, '', 'pedro@gms', '7e3759aa1c6f94082beed27930be292d3207e5b5e3e5bab2a5eacf4b38053a54', '2021-11-05 19:07:31.352780', '', '', 0);
INSERT INTO tb_usuario (id_usuario, nome, cpf, telefone, email, senha, data_nascimento, tipo_sanguineo, alergia, endereco_id) VALUES (16, 'leonardo', NULL, '', 'pedro@gmss', '7e3759aa1c6f94082beed27930be292d3207e5b5e3e5bab2a5eacf4b38053a54', '2021-11-05 19:07:31.352780', '', '', 0);
INSERT INTO tb_usuario (id_usuario, nome, cpf, telefone, email, senha, data_nascimento, tipo_sanguineo, alergia, endereco_id) VALUES (17, 'LucianoCoelho', NULL, '', 'abcbolinhas@gmail.com', 'ea264bb246225215621450677b983e8d0f1cbec477c2acc21bbefce41d5cf8b4', '2021-11-05 19:16:49.733124', '', '', 0);
INSERT INTO tb_usuario (id_usuario, nome, cpf, telefone, email, senha, data_nascimento, tipo_sanguineo, alergia, endereco_id) VALUES (18, 'asdasd', NULL, '', 'asdasdasd@gmail.com', '7e3759aa1c6f94082beed27930be292d3207e5b5e3e5bab2a5eacf4b38053a54', '2021-11-06 21:04:21.219911', '', '', 0);
INSERT INTO tb_usuario (id_usuario, nome, cpf, telefone, email, senha, data_nascimento, tipo_sanguineo, alergia, endereco_id) VALUES (19, 'João', '912.332.123.12', '(49)9923-98433', 'joao@gmail.com', '7e3759aa1c6f94082beed27930be292d3207e5b5e3e5bab2a5eacf4b38053a54', '2021-11-09 13:11:53.787551', 'O-', 'Anti-Inflamatorios', 22);

-- Index: tb_usuario_UQ__tb_usuar__D836E71F33E47992
CREATE UNIQUE INDEX tb_usuario_UQ__tb_usuar__D836E71F33E47992 ON tb_usuario (
    cpf DESC
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
