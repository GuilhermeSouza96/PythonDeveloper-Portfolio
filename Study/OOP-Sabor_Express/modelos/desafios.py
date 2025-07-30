# class Musica:
#     musicas = []

#     def __init__(self, nome, artista, duracao):
#         self.nome = nome
#         self.artista = artista
#         self.duracao = int(duracao)
#         Musica.musicas.append(self)
    
#     def __str__(self):
#         return f'{self.nome} | {self.artista} | {self.duracao} segundos'
    
#     def listar_musicas():
#         for musica in Musica.musicas:
#             print(f'{musica.nome} | {musica.artista} | {musica.duracao} segundos')

# musica1 = Musica('November Rain', 'Guns N Roses', 355)
# musica2 = Musica('Cry Thunder', 'Dragonforce', 200)
# musica3 = Musica('So far Away', 'Avenged Sevenfold', 300)

# Musica.listar_musicas()


class Pessoa:
    def __init__(self, nome = '', idade = 0, profissao = ''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'
    
    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}! Trabalho com {self.profissao}'
        else:
            return f'Olá, sou {self.nome}'
        
    def aniversario(self):
        self.idade += 1


pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=22)

print("Informações Iniciais:")
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

pessoa1.aniversario()
pessoa3.aniversario()

print("Informações após aniversário:")
print(pessoa1)
print(pessoa3)
print()

print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)