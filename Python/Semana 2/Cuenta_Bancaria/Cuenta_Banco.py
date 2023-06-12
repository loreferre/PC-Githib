class CuentaBancaria:
    todas_las_cuentas = []
    
    def __init__(self, tasa_int=0.01, balance=0.0):
        self.tasa_int = tasa_int
        self.balance = balance
        self.__class__.todas_las_cuentas.append(self)

    def deposito(self, amount):
        self.balance += amount
        print(f'Balance actual: ${self.balance}')
        return self
    
    def retiro(self, amount):
        if self.puede_retirar(amount):
            self.balance -= amount
            print(f'Balance actual: ${self.balance}')
        else:
            print("Fondos insuficientes")
        return self

    def generar_interes(self):
        self.balance += self.balance * self.tasa_int
        print(f'Interés generado: ${self.balance * self.tasa_int}, Balance actual: ${self.balance}')
        return self
    
    def puede_retirar(self, amount):
        return (self.balance - amount) >= 0

    def mostrar_info_cuenta(self):
        print(f'Balance: ${self.balance}, Tasa de interés: {self.tasa_int*100}%')
        return self
    
    @classmethod
    def mostrar_todas_las_cuentas(cls):
        for cuenta in cls.todas_las_cuentas:
            cuenta.mostrar_info_cuenta()



cuenta1 = CuentaBancaria(0.02,500)
cuenta1.deposito(100).deposito(200).deposito(700).retiro(50).generar_interes().mostrar_info_cuenta()

print("------------")

cuenta2 = CuentaBancaria(0.03, 1000)
cuenta2.deposito(1200).deposito(400).retiro(70).retiro(100).retiro(600).retiro(300).generar_interes().mostrar_info_cuenta()

print("------------")

CuentaBancaria.mostrar_todas_las_cuentas()