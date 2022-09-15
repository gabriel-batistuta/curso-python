x=1 # int
x="CFB Cursos" #string
x=15.6 # float
x=True # bool
n1=5;n2=2;x=complex(1j)
x=["Carro", "Aviao", "Navio",1,58.3,True] # List / Array (seus valores podem mudar)
x=("Carro", "Aviao", "Navio",1,58.3,True) # Tupla (não se modificam)

x=range(0,100,1) # List
# range faz uma lista entre os numeros pedidos

x={ #Dictionary
    "canal":"CFB Cursos",
    "curso":"Curso de Python",
    "Nome":"Gabriel"
}
x={5,7,4,5,7,4,8} #set // não repete valores
x=frozenset({5,7,4,5,7,4,8}) # set só que não pode mudar os valores das variaveis
print("Valor: "+str(x))
# print("Valor: "+x["canal"])
print("Tipo: "+str(type(x)))