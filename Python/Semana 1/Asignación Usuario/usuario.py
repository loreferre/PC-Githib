class Usuario:
    nombre_banco = "Primer Dojo Nacional"

    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.balance_cuenta = 0

    def hacer_deposito(self, amount):
        self.balance_cuenta += amount
        print(f'Usuario: {self.name}, Balance: ${self.balance_cuenta}')

    def hacer_retiro(self, amount):
        if amount <= self.balance_cuenta:
            self.balance_cuenta -= amount
        else:
            print(print(f'Usuario: {self.name}, Balance: ${self.balance_cuenta}'))

    def mostrar_balance_usuario(self):
        print(f'Usuario: {self.name}, Balance: ${self.balance_cuenta}')

    def transferir_dinero(self, other_user, amount):
        if amount <= self.balance_cuenta:
            self.balance_cuenta -= amount
            other_user.hacer_deposito(amount)
        else:
            print("Fondos insuficientes")

lorena  = Usuario('Lorena', 'lorena@example.com')
algo  = Usuario('Sra. Algo', 'algo@example.com')
nose = Usuario('Sr.Nose', 'nose@example.cl')

lorena.hacer_deposito(100)
lorena.hacer_deposito(200)
lorena.hacer_deposito(700)
lorena.hacer_retiro(50)
lorena.mostrar_balance_usuario()

nose.hacer_deposito(50)
nose.hacer_deposito(800)
nose.hacer_retiro(550)
lorena.hacer_retiro(50)
nose.mostrar_balance_usuario()

algo.hacer_deposito(1000)
algo.hacer_retiro(156)
algo.hacer_retiro(390)
algo.hacer_retiro(15)
algo.mostrar_balance_usuario()

lorena.transferir_dinero(algo, 50)
algo.mostrar_balance_usuario()




