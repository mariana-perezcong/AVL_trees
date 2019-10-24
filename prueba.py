__author__ = 'mperezcs'

from ArbolAVL import ArbolAVL

arbol=ArbolAVL()

arbol.inserta(100)
arbol.inserta(300)
arbol.inserta(400)
arbol.inserta(350)
arbol.inserta(375)
arbol.inserta(50)
arbol.inserta(200)
arbol.inserta(360)

print(arbol.imprimeNiv())

arbol.elimina(300)
arbol.elimina(360)
arbol.elimina(350)
print(arbol.imprimeNiv())


"""
a=arbol.getRaiz()
b=a.left.node
d=b.left.node
e=b.right.node

c=a.right.node
f=c.left.node
g=c.right.node


print(a.key)
print(b.key, c.key)
print(d.key,e.key,f.key,g.key)"""
