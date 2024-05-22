'''
class Pessoas:


    def __init__(self,nome,idade,peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def envelhecer(self):
        self.idade += 1 
        if self.idade < 21:
            self.crescer += (0.05) 
        return self.idade
    def engordar(self, kilos):
        self.peso += kilos
        return self.peso
    def emagrecer(self,kilos_perdidos):
        self.peso -= kilos_perdidos
        return self.peso
    def crescer(self, anos ):
        if self.idade < 21:
            self.altura += (0.05) * anos
        return self.altura
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.anos = anos
        self.idade += anos
        print('\nA pessoa envelheceu ',anos,' anos\nA idade atual é ',self.idade,' anos')

    def engordar(self, pesagem):
        self.peso += pesagem
        print('\nA pessoa engordou ',pesagem,' kg\nO peso atual é',round(self.peso),'kg')

    def emagrecer(self, pesagem):
        self.peso -= pesagem
        print('\nA pessoa emagreceu ',pesagem,' kg\nO peso atual é',round(self.peso),'kg')

    def crescer(self, anos):
        self.idade += 1
        if self.idade < 21:
            crescimento = 0.05 * anos
            self.altura += crescimento
            print('\nA pessoa cresceu ',crescimento,'m\nA altura atual é',self.altura,'m')
        else:
            print('\nA pessoa não cresceu')



pessoa_1 = Pessoas ('Mayk', 15, 76.10, 1.75)
print (pessoa_1.nome)
pessoa_1.envelhecer(5)
pessoa_1.engordar(10.1)
pessoa_1.emagrecer(5)
pessoa_1.crescer(4)
'''

class Pessoa :

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1 
        if self.idade < 21:
            self.crescer(0.5)

    def engordar(self, peso):
        self.peso -= peso

    def emagrecer(self, peso):
        self.peso -= peso
        return self.peso
    
    def crescer(self, altura):
        self.altura += altura

    def __str__(self):
        return f"Nome: {self.nome}, idade {self.idade}, peso {self.peso}, altura {self.altura} "

pesso1 = Pessoa ("João", 20, 150, 1.65)     
print("Dados Iniciais")
print(pesso1)

pesso1.envelhecer()
pesso1.engordar(10)

print("Dados após envelhecer e engordar: ")
print(pesso1)

        