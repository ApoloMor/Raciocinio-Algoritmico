"""
Funções de objeto
fazer uma função que não modifica um objeto
ex: elevar um numero  ao quadrado
"""
def quadrado(num) #toda função/variavel dentro de uma def é local, ou seja esta só pode ser usada dentro de def
    quad = num * num
    return quad 
n = 3
q = quadrado(n)
print("O quadrado de {n} é {q}")
