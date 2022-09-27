carros=["HRV","Golf","Argo","Focus"] # List
carros.append("Fit")
carros.append("Fusion")
carros.append("Polo")

'''

carros.remove("Palio") # remove o elemento que tiver esse conteudo

'''

carros.pop() # deleta o ultimo elemento da lista

del carros[2] # deleta o elemento pelo indice escolhido

'''
carros.clear() # limpa todos os elementos da lista
'''

carros2=list(carros) # copia a lista inteira de um array para outra

print(carros2)

carros2=["Fusca","147","Brasilia","Celta"]

carros3=carros+carros2

print(str(len(carros3)) + " carros na lista") 

print(carros3)