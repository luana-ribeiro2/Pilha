class _No:
    '''
    Classe auxiliar Nó.
    '''
    def __init__(self, valor, proximo = None):
        '''
        Para esse tipo de fila é denecessário o uso de encadeamento duplo.
        '''
        self.valor = valor
        self.proximo = proximo
    
    def __repr__(self):
        return "_No({})".format(self.valor.__repr__())
    
    def __str__(self):
        return self.valor.__str__()

class Pilha:
    '''
    Classe principal pilha. Pode ser construída vazia ou a partir de um
    iterável. É possível limitar o tamanho da fila com o uso do kwarg 'lim'.
    Na pilha, a operação de inserção é chamada de empilhar (push) e a de
    remoção de desempilhar (pop). Além dessas, também há a operação de puxar
    (pull) que move um nó para o topo da pilha.
    '''
    def __init__(self, iteravel = None, **kwargs):
        self.primeiro = None
        self.limite = kwargs.get("lim", -1)
        self.__tam = 0
        if iteravel is not None:
            for item in iteravel:
                self.empilhar(item)
    
    def empilhar(self, item):
        '''
        Numa pilha a inserção (ou empilhamento) se dá sempre no início.
        '''
        if self.__tam < self.limite or self.limite == -1:
            self.primeiro = _No(item, self.primeiro)
            self.__tam += 1
        else:
            return ValueError ("pilha cheia")
    
    def desempilhar(self):
        '''
        A operação de remoção (desempilhamento) acontece sempre no primeiro
        elemento da pilha.
        '''
        if self.primeiro is None:
            raise IndexError ("pilha vazia")
        aux = self.primeiro
        self.primeiro = self.primeiro.proximo
        aux.proximo = None
        valor = aux.valor
        del aux
        self.__tam -= 1
        return valor

    def __str__(self):
        atual = self.primeiro
        msg = ''
        while atual is not None:
            if msg: msg += ' -> '
            msg += repr(atual.valor)
            atual = atual.proximo
        return "[{}]".format(msg)
    
if __name__ == '__main__':
    Pilhinha = Pilha()
    Pilhinha.empilhar(2)
    Pilhinha.empilhar(40)
    Pilhinha.empilhar(50)
    Pilhinha.empilhar(55)
    print(Pilhinha)
    Pilhinha.desempilhar()
    Pilhinha.desempilhar()
    print(Pilhinha)
    Pilhinha.empilhar(7)
    Pilhinha.empilhar(3)
    print(Pilhinha)
    Pilhinha.desempilhar()
    Pilhinha.desempilhar()
    Pilhinha.desempilhar()
    Pilhinha.empilhar(1)
    Pilhinha.empilhar(4)
    Pilhinha.empilhar(6)
    Pilhinha.empilhar(9)
    Pilhinha.desempilhar()
    print(Pilhinha)