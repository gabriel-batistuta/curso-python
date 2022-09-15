# definição de escopo e global

"""
se a variavel estiver contida em uma função ela so pode ser acessada dentro da função a menos que ela tenha sido declarada como global anteriormente
"""
def cn():
    global canal
    canal="CFB Cursos"
cn()

print(canal)