class pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura



    def apresentacao(self):
        print(f"O nome da pessoa consultada e {self.nome}; \nA idade dele(a) e: {self.idade}")

    def fazer_aniversario(self):
        self.idade +=1
        print(f"Feliz aniversario, {self.nome}!!! Sua nova idade agora e{self.idade}.")

eu = pessoa("thiago", "19", "79kg", "1.80")

vc = pessoa("junior", "20", "75kg", "1.79")

eu.apresentacao()