class Usuario:
    nombre_banco = "Primer Dojo Nacional"

    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.balance_cuenta = 0

    def hacer_deposito(self, amount):
        self.balance_cuenta += amount
        print(f'Usuario: {self.name}, Balance: ${self.balance_cuenta}')
        return self

    def hacer_retiro(self, amount):
        if amount <= self.balance_cuenta:
            self.balance_cuenta -= amount
        else:
            print(f'Usuario: {self.name}, Balance: ${self.balance_cuenta}')
        return self
        
    def mostrar_balance_usuario(self):
        print(f'Usuario: {self.name}, Balance: ${self.balance_cuenta}')
        return self


lorena  = Usuario('Lorena', 'lorena@example.com')

lorena.hacer_deposito(100).hacer_deposito(200).hacer_deposito(700).hacer_retiro(50).mostrar_balance_usuario().mostrar_balance_usuario()






