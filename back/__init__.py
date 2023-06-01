class Banco:
    def _init_(self, name):
        self.name = str(name)
    
    def function(x):
        return x
    

class ContaCorrente(Banco):
    def _init_(self, name):
        self.name = str(name)
    
    def function(x):
        return x


class ContaPoupança(Banco):
    def _init_(self, name):
        self.name = str(name)
    
    def function(x):
        return x


class Pessoa:
    def _init_(self, nome, sexo, cpf):
        self.nome = str(name)
        self.sexo = str(name)
        self.cpf = int(cpf)
        self.banco = ContaCorrente(Banco)
				