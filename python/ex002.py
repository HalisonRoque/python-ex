def remove(self, valor):
    if self.head.data == valor:
        self.head = self.head.nextitem
    else:
        before = None
        navegar = self.head
        while navegar and navegar.data != valor:
            before = navegar
            navegar = navegar.nextitem
            if navegar:
                before.nextitem = navegar.nextitem
            else:
                before.nextitem = None


a = float(input('valor 1: '))
b = float(input('valor 2: '))
remove(a, b)
print(remove)
