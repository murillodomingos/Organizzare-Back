def create_melao(): # <- funcao
    return Fruta('melao', 1000, 10)

class Fruta: # <- classe
    def __init__(self, nome, peso_g, preco_kg): # <- construtor
        self.nome = nome # <- atributo
        self.peso_g = peso_g
        self.preco_kg = preco_kg

    def get_price(self): # <- metodo
        return "R$ %.2f"%( self.peso_g * self.preco_kg / 1000)

    def get_pounds(self):
        return "%d pounds"%(self.peso_g * 236)

medida_1 = Fruta("maçã", 200, 1.00) # <- objeto (instancia da classe usando o construtor)

print(medida_1.get_price()) # <- chamada do metodo
print(medida_1.nome) # <- veficacao do atributo

melao = create_melao() # <- uma funcao pode retornar um objeto
print(melao.nome)