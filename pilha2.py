class Pilha:
    def __init__(self):
        self.lista = []
        self.__size = 0
            

    def __repr__(self):
        return repr(self.lista)

    def __str__(self):
        return str(self.lista)

    def __len__(self):
        return (self.__size)


    def push(self, item):
        self.lista.insert(0, item)
        self.__size += 1

    def pop(self):
        item = self.lista[0]
        del self.lista[0]
        self.__size -= 1
        return item

teste = Pilha()
n = int(input(''))
conjuntoN = 1
aux = True
while n > 0:
    com = input("")
    comando1 = com.split(' ')
    if aux == True:
        print('Conjunto #{}'.format(conjuntoN))
        aux = False
    for x in comando1:
        if x == '':
            pass
        else:
            
            if x == 'return' and len(teste) == 1:
                
                
                print(teste.lista[0])
                teste.pop()
                conjuntoN +=1
                n-=1
                aux = True

            elif x == 'return':
                print(teste.lista[0])
                teste.pop()
                
            
                
            else:
                teste.push(x)
            

        

