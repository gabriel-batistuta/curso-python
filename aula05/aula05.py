import random
# Casting - Conversão de tipos

num_i=10
num_f=5.2
num_c=1j

num_r=[ #List / Array
    random.randrange(0,59),
       random.randrange(0,59),
       random.randrange(0,59),
       random.randrange(0,59),
       random.randrange(0,59),
       ]

# random (aleatorio)

x=num_r


print("Valor: "+ str(num_r[0]) + " - Tipo: "+ str(type(x)))
print("Valor: "+ str(num_r[1]) + " - Tipo: "+ str(type(x)))
print("Valor: "+ str(num_r[2]) + " - Tipo: "+ str(type(x)))