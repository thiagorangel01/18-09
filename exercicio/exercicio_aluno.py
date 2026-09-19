class aluno:
    def __init__(self, matricula, nome, nota1, nota2, nota3, nota4, nota5,):
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        self.nota5 = nota5
        

    def calcular_media(self):
        self.media = (self.nota1 + self.nota2 + self.nota3 + self.nota4 + self.nota5) /5
        print(f"Sau matricula e: {self.matricula} \nSeu nome e: {self.nome} sua media foi: {self.media}")

    def aprovado(self):
        if self.media >= 7:
            print(f"Voce foi aprovado")
        else:
            print("Voce foi reprovado")
aluno1 = aluno("01010", "Thiago", 10, 10, 9, 9.5, 8)
aluno2 = aluno("10010", "junior", 1, 1.3, 0, 0.9, 2.3)

aluno1.calcular_media()
aluno1.aprovado()

aluno2.calcular_media()
aluno2.aprovado()