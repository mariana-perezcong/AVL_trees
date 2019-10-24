__author__ = 'mperezcs'
from NodoAVL import Node
from Queue import Queue

class ArbolAVL():
    def __init__(self, *args):
        self.node = None
        self.altura = -1
        self.balance = 0;

        if len(args) == 1:
            for i in args[0]:
                self.inserta(i)

    def altura(self):
        if self.node:
            return self.node.altura
        else:
            return 0

    def inserta(self, key):
        nodo = self.node

        nuevo = Node(key)

        if nodo is None:
            self.node = nuevo
            self.node.left =ArbolAVL()
            self.node.right =ArbolAVL()

        elif key < nodo.key:
            self.node.left.inserta(key)

        elif key > nodo.key:
            self.node.right.inserta(key)

        self.balancear()

    def balancear(self):
        self.actAltura(False)
        self.actualizaFe(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.rotaIzq()
                    self.actAltura()
                    self.actualizaFe()
                self.rotaDer()
                self.actAltura()
                self.actualizaFe()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rotaDer()
                    self.actAltura()
                    self.actualizaFe()
                self.rotaIzq()
                self.actAltura()
                self.actualizaFe()


    def rotaDer(self):
        alpha = self.node
        beta = self.node.left.node
        gamma = beta.right.node

        self.node = beta
        beta.right.node = alpha
        alpha.left.node = gamma


    def rotaIzq(self):
        alpha = self.node
        beta = self.node.right.node
        gamma = beta.left.node

        self.node = beta
        beta.left.node = alpha
        alpha.right.node = gamma


    def actAltura(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.actAltura()
                if self.node.right != None:
                    self.node.right.actAltura()

            self.altura = max(self.node.left.altura,
                              self.node.right.altura) + 1
        else:
            self.altura = -1

    def actualizaFe(self, recurse=True):
        if not self.node is None:
            if recurse:
                if self.node.left != None:
                    self.node.left.actualizaFe()
                if self.node.right != None:
                    self.node.right.actualizaFe()

            self.balance = self.node.left.altura - self.node.right.altura
        else:
            self.balance = 0

    def elimina(self, key):
        if self.node is not None:
            if self.node.key == key:
                if self.node.left.node is None and self.node.right.node is None:
                    self.node = None
                elif self.node.left.node is None:
                    self.node = self.node.right.node
                elif self.node.right.node is None:
                    self.node = self.node.left.node
                else:
                    sucIn = self.sucInorden(self.node)
                    if sucIn is not None:
                        self.node.key = sucIn.key
                        self.node.right.elimina(sucIn.key)

                self.balancear()
                return
            elif key < self.node.key:
                self.node.left.elimina(key)
            elif key > self.node.key:
                self.node.right.elimina(key)

            self.balancear()
        else:
            return

    def sucInorden(self, nodo):
        nodo = nodo.right.node
        if nodo is not None:
            while nodo.left is not None:
                if nodo.left.node is None:
                    return nodo
                else:
                    nodo = nodo.left.node
        return nodo

    def checaBalanceado(self):
        if self is None or self.node is None:
            return True
        self.actAltura()
        self.actualizaFe()
        return ((abs(self.balance) < 2) and self.node.left.checaBalanceado() and self.node.right.checaBalanceado())

    def imprimeIn(self):
        if self.node is None:
            return
        self.node.left.imprimeIn()
        print(self.node.key)
        self.node.right.imprimeIn()

    def busca(self, elem):
        actual=self.node
        while(actual is not None and actual.key is not elem ):
            if(elem<actual.key):
                actual=actual.left.node
            else:
                actual=actual.right.node
        if actual is None:
            return False
        else:
            return True

    def getRaiz(self):
        return self.node


    def imprimeNiv(self):
        s=""
        nodo= self.node
        if(nodo is None):
            return
        q1=Queue()
        q2=Queue()
        q1.enqueue(self.node)
        while(not q1.isEmpty()) or (not q2.isEmpty()):
            while(not q1.isEmpty()):
                nodo=q1.dequeue()
                s=s+str(nodo.key)+" "
                #print(nodo.key)
                if(nodo.left.node is not None):
                    q2.enqueue(nodo.left.node)
                if(nodo.right.node is not None):
                    q2.enqueue(nodo.right.node)
            s=s+"\n"
            #print("\n")

            while(not q2.isEmpty()):
                nodo=q2.dequeue()
                s=s+str(nodo.key)+" "
                #print(nodo.key)
                if(nodo.left.node is not None):
                    q1.enqueue(nodo.left.node)
                if(nodo.right.node is not None):
                    q1.enqueue(nodo.right.node)
            s=s+"\n"
            #print("\n")

        return s
