from hashlib import sha3_256

class Funcoes(object):
    @staticmethod
    def cifrarSenha(senha):
        return sha3_256(senha.encode('utf-8')).hexdigest()