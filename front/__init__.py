class Banco:
    def _init_(self, name):
        self.name = str(name)
    
    def function(x):
        return x
    

class Conta_Corrente(Banco):
    def _init_(self, name):
        self.name = str(name)
    
    def function(x):
        return x


class Conta_Poupança(Banco):
    def _init_(self, name):
        self.name = str(name)
    
    def function(x):
        return x


class Pessoa_A:
    def _init_(self, nome, sexo, cpf):
        self.nome = str(name)
        self.sexo = str(name)
        self.cpf = int(cpf)
        self.banco = Conta_Corrente(banco)